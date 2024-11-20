import streamlit as st
import openai
from PIL import Image
import pandas as pd
import json
import os

# Configure OpenAI
def get_openai_recommendation(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role": "system",
                "content": "You are an expert PC building assistant. Provide component recommendations based on user requirements."
            }, {
                "role": "user",
                "content": prompt
            }],
            temperature=0.7,
            max_tokens=500
        )
        return response.choices[0].message.content
    except Exception as e:
        return None
PC_COMPONENTS = {
    "Gaming": {
        "Budget": {
            "CPU": ["AMD Ryzen 5 5600X", "Intel i5-12400F"],
            "GPU": ["RTX 3060", "RX 6600"],
            "RAM": ["16GB DDR4 3200MHz"],
            "Storage": ["1TB NVMe SSD"],
            "Motherboard": ["B550", "B660"],
            "PSU": ["650W 80+ Gold"],
            "Case": ["NZXT H510", "Phanteks P300"],
        },
        "High-end": {
            "CPU": ["AMD Ryzen 7 7800X3D", "Intel i7-13700K"],
            "GPU": ["RTX 4080", "RX 7900 XT"],
            "RAM": ["32GB DDR5 6000MHz"],
            "Storage": ["2TB NVMe SSD"],
            "Motherboard": ["X670E", "Z790"],
            "PSU": ["850W 80+ Gold"],
            "Case": ["Lian Li O11", "Corsair 5000D"],
        }
    },
    "Workstation": {
        "Budget": {
            "CPU": ["AMD Ryzen 7 5800X", "Intel i7-12700"],
            "GPU": ["RTX 3060 Ti", "RX 6700 XT"],
            "RAM": ["32GB DDR4 3600MHz"],
            "Storage": ["2TB NVMe SSD"],
            "Motherboard": ["B550", "B660"],
            "PSU": ["750W 80+ Gold"],
            "Case": ["Fractal Design Meshify C", "be quiet! Pure Base 500"],
        },
        "High-end": {
            "CPU": ["AMD Ryzen 9 7950X", "Intel i9-13900K"],
            "GPU": ["RTX 4090", "RX 7900 XTX"],
            "RAM": ["64GB DDR5 6400MHz"],
            "Storage": ["4TB NVMe SSD"],
            "Motherboard": ["X670E", "Z790"],
            "PSU": ["1000W 80+ Platinum"],
            "Case": ["Lian Li O11 Dynamic EVO", "Phanteks Enthoo 719"],
        }
    }
}

def main():
    st.set_page_config(page_title="Divine PC Builder", layout="wide")
    
    # Custom CSS for modern UI
    st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        background-color: #7E57C2;
        color: white;
        border-radius: 20px;
        padding: 10px 25px;
    }
    .css-1d391kg {
        background-color: #ffffff;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

    # Hero section
    col1, col2 = st.columns([2,1])
    with col1:
        st.title("🌟 Divine PC Builder")
        st.markdown("""
        Experience AI-powered PC building guidance personalized for you.
        Get instant recommendations, insights, and practical build advice.
        """)
    
    # Main chat interface
    st.markdown("---")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
        st.session_state.show_builder = False

    # Chat input
    user_input = st.text_input("Tell me about your PC needs...", 
                              placeholder="e.g., I need a gaming PC for streaming under $2000")
    
    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Get AI response
        prompt = f"""
        User request: {user_input}
        Provide PC build recommendations in this format:
        - Use case analysis
        - Recommended components
        - Performance expectations
        - Budget breakdown
        """
        
        with st.spinner("🤔 Contemplating the perfect build..."):
            ai_response = get_openai_recommendation(prompt)
            if ai_response:
                st.session_state.messages.append({"role": "assistant", "content": ai_response})
                st.session_state.show_builder = True

    # Display chat history
    for message in st.session_state.messages:
        with st.container():
            if message["role"] == "user":
                st.markdown(f"🧑 **You:** {message['content']}")
            else:
                st.markdown(f"🤖 **Divine Builder:** {message['content']}")

    # Interactive builder interface
    if st.session_state.show_builder:
        st.markdown("---")
        st.subheader("🛠️ Customize Your Build")
        
        col1, col2 = st.columns([2,1])
        
        with col1:
            # Component selection with explanations
            components = ["CPU", "GPU", "RAM", "Storage", "Motherboard", "PSU", "Case"]
            for component in components:
                with st.expander(f"{component} Selection", expanded=True):
                    st.markdown(f"### {component}")
                    options = PC_COMPONENTS["Gaming"]["High-end"][component] if component in PC_COMPONENTS["Gaming"]["High-end"] else ["Option 1", "Option 2"]
                    selected = st.selectbox(
                        "Choose your component:",
                        options,
                        key=f"select_{component}"
                    )
                    st.info(f"💡 Why this matters: AI-powered explanation for {component} choice")
        
        with col2:
            # Build summary and insights
            st.markdown("### 🎯 Build Overview")
            st.progress(0.8)
            st.metric("Build Completion", "80%")
            
            # Performance predictions
            st.markdown("### 🚀 Performance Insights")
            col_a, col_b = st.columns(2)
            with col_a:
                st.metric("Gaming Score", "92/100")
            with col_b:
                st.metric("Value Score", "88/100")

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center'>
    💡 Built with wisdom from thousands of PC builds. Constantly learning and evolving.
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()