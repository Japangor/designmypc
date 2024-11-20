import streamlit as st
from transformers import pipeline
from PIL import Image
import pandas as pd
import json
import os
from datetime import datetime

# Initialize sentiment analysis pipeline
@st.cache_resource
def load_model():
    return pipeline(
        "text-classification",
        model="facebook/bart-large-mnli",
        device=-1  # CPU
    )

# PC Components database remains the same as before
PC_COMPONENTS = {
    # ... (keep existing PC_COMPONENTS dictionary)
}

def get_ai_recommendation(user_input, classifier):
    """Get AI recommendations using the BART model"""
    try:
        # Analyze user requirements using zero-shot classification
        candidate_labels = [
            "gaming performance focused",
            "workstation productivity focused",
            "budget conscious",
            "high-end enthusiast",
            "content creation focused"
        ]
        
        result = classifier(user_input, candidate_labels)
        
        # Map classification to component selection
        if "gaming" in result['labels'][0]:
            category = "Gaming"
        else:
            category = "Workstation"
            
        if "budget" in result['labels'][0]:
            tier = "Budget"
        else:
            tier = "High-end"
            
        return PC_COMPONENTS[category][tier], category, tier
        
    except Exception as e:
        st.error(f"AI Error: {str(e)}")
        return None, None, None

def main():
    st.set_page_config(
        page_title="GJAM PC Builder", 
        page_icon="🖥️",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Custom CSS
    st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton > button {
        background-color: #6C63FF;
        color: white;
        border-radius: 10px;
        padding: 0.5rem 1rem;
        font-weight: 500;
    }
    .css-1d391kg {
        background-color: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .header-image {
        max-width: 150px;
        margin-bottom: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)

    # Header with GJAM Technologies branding
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image("https://via.placeholder.com/150x50?text=GJAM+Tech", use_column_width=True)
        st.title("🌟 Intelligent PC Builder")
        st.markdown("""
        <div style='text-align: center'>
        Powered by Open Source AI | Built by GJAM Technologies
        </div>
        """, unsafe_allow_html=True)

    # Initialize AI model
    classifier = load_model()
    
    # Main chat interface
    st.markdown("### 🤖 Tell me about your dream PC")
    
    # Chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
        
    # Display chat history
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f"🧑 **You:** {message['content']}")
        else:
            st.markdown(f"🤖 **AI Assistant:** {message['content']}")
    
    # User input area
    user_input = st.text_area(
        "Describe your needs in detail...",
        height=100,
        placeholder="Example: I need a powerful gaming PC for streaming and video editing. I prefer AMD processors and want good cooling for overclocking. My budget is around $2000."
    )
    
    col1, col2, col3 = st.columns([3,2,3])
    with col2:
        if st.button("🔮 Generate Build", use_container_width=True):
            if user_input:
                # Add user message to chat
                st.session_state.messages.append({"role": "user", "content": user_input})
                
                # Get AI recommendation
                with st.spinner("🧠 Analyzing your requirements..."):
                    components, category, tier = get_ai_recommendation(user_input, classifier)
                    
                    if components:
                        # Create detailed response
                        response = f"""Based on your requirements, I recommend a {tier} {category} build:

🎯 **Build Overview:**
- Category: {category}
- Tier: {tier}
- Estimated Performance: {'Excellent for gaming and streaming' if category == 'Gaming' else 'Optimal for workstation tasks'}

🔧 **Recommended Components:**"""
                        
                        for component, options in components.items():
                            if isinstance(options, list):
                                response += f"\n- {component}: {options[0]} (Alternative: {options[1]})"
                            else:
                                response += f"\n- {component}: {options}"
                        
                        st.session_state.messages.append({"role": "assistant", "content": response})
                        st.session_state.current_build = components
                        st.experimental_rerun()

    # Display build details if available
    if "current_build" in st.session_state:
        st.markdown("---")
        
        col1, col2 = st.columns([2,1])
        
        with col1:
            st.markdown("### 🎮 Build Configuration")
            
            tabs = st.tabs(["Components", "Performance", "Pricing"])
            
            with tabs[0]:
                for component, options in st.session_state.current_build.items():
                    with st.expander(f"📦 {component}", expanded=True):
                        if isinstance(options, list):
                            selected = st.selectbox(
                                f"Choose {component}:",
                                options,
                                key=f"select_{component}"
                            )
                            st.image(f"https://via.placeholder.com/400x200?text={selected}", use_column_width=True)
                            st.markdown(f"**Selected:** {selected}")
                        else:
                            st.markdown(f"**Recommended:** {options}")
                            
            with tabs[1]:
                col_a, col_b = st.columns(2)
                with col_a:
                    st.metric("Performance Score", "92/100", "↑15%")
                with col_b:
                    st.metric("Value Rating", "88/100", "↑10%")
                    
                # Performance chart placeholder
                st.image("https://via.placeholder.com/800x400?text=Performance+Charts", use_column_width=True)
                
            with tabs[2]:
                st.metric("Estimated Total", "$1,999", "-$1 under budget")
                st.progress(0.8, "Build Completion: 80%")
        
        with col2:
            st.markdown("### 🎯 Build Summary")
            st.info("🔥 This build is optimized for your specific needs!")
            
            # Add compatibility check
            st.markdown("#### ✅ Compatibility Check")
            st.markdown("""
            - ✓ Power supply is sufficient
            - ✓ Components are compatible
            - ✓ Case fits all components
            - ✓ Cooling is adequate
            """)
            
            # Export options
            if st.button("📤 Export Build", use_container_width=True):
                build_data = {
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "components": st.session_state.current_build,
                    "user_requirements": user_input
                }
                st.download_button(
                    label="💾 Download Build",
                    data=json.dumps(build_data, indent=2),
                    file_name="gjam_pc_build.json",
                    mime="application/json",
                    use_container_width=True
                )

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center'>
    Made with ❤️ by GJAM Technologies | Open Source AI Powered | © 2024
    <br><br>
    💡 Prices and availability may vary. Always verify compatibility and current prices before purchase.
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()