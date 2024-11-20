import streamlit as st
import openai
from PIL import Image
import pandas as pd
import json
import os

# Sample component database (in practice, you'd want to use a real database)
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

def get_ai_recommendation(user_requirements):
    """Simulate AI recommendations (replace with actual OpenAI API in production)"""
    use_case = user_requirements["use_case"]
    budget = user_requirements["budget"]
    
    if budget <= 1000:
        tier = "Budget"
    else:
        tier = "High-end"
    
    components = PC_COMPONENTS[use_case][tier]
    return components

def calculate_price_estimate(components):
    """Simulate price calculation"""
    # In practice, you'd want to fetch real prices from an API
    base_prices = {
        "Budget": {
            "Gaming": 800,
            "Workstation": 1000
        },
        "High-end": {
            "Gaming": 2000,
            "Workstation": 3000
        }
    }
    return base_prices["High-end" if "High-end" in str(components) else "Budget"]["Gaming" if "Gaming" in str(components) else "Workstation"]

def main():
    st.set_page_config(page_title="AI PC Builder", layout="wide")
    
    # Title and introduction
    st.title("🖥️ AI PC Builder")
    st.markdown("""
    Let's build your perfect PC! Tell me what you need, and I'll recommend the best components.
    """)
    
    # Sidebar for user input
    with st.sidebar:
        st.header("Your Requirements")
        
        use_case = st.selectbox(
            "What will you use your PC for?",
            ["Gaming", "Workstation"],
            help="This helps me recommend the right components"
        )
        
        budget = st.slider(
            "What's your budget? (USD)",
            min_value=500,
            max_value=5000,
            value=1500,
            step=100,
            help="Slide to set your maximum budget"
        )
        
        preferences = st.multiselect(
            "Any specific preferences?",
            ["Ray Tracing", "Quiet Operation", "RGB Lighting", "Overclock-ready", "Small Form Factor"],
            help="Select any specific features you'd like"
        )
        
        if st.button("Generate Build 🚀", use_container_width=True):
            user_requirements = {
                "use_case": use_case,
                "budget": budget,
                "preferences": preferences
            }
            
            # Get AI recommendations
            with st.spinner("🤔 Thinking of the perfect build for you..."):
                recommended_components = get_ai_recommendation(user_requirements)
                
                # Store in session state
                st.session_state.recommendations = recommended_components
                st.session_state.price_estimate = calculate_price_estimate(recommended_components)
                st.session_state.show_results = True
    
    # Main content area
    if "show_results" in st.session_state and st.session_state.show_results:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.header("Recommended Build")
            
            # Display components in an organized way
            for component, options in st.session_state.recommendations.items():
                with st.expander(f"📦 {component}", expanded=True):
                    if isinstance(options, list):
                        selected = st.selectbox(
                            f"Select your preferred {component}:",
                            options,
                            key=f"select_{component}"
                        )
                        st.markdown(f"**Selected:** {selected}")
                    else:
                        st.markdown(f"**Recommended:** {options}")
        
        with col2:
            st.header("Build Summary")
            st.metric(
                "Estimated Total",
                f"${st.session_state.price_estimate:,}",
                delta=f"${budget - st.session_state.price_estimate:,} from budget"
            )
            
            # Performance metrics
            st.subheader("Expected Performance")
            if use_case == "Gaming":
                col_fps, col_res = st.columns(2)
                with col_fps:
                    st.metric("Avg. FPS (1440p)", "144+" if "High-end" in str(st.session_state.recommendations) else "60+")
                with col_res:
                    st.metric("Max Resolution", "4K" if "High-end" in str(st.session_state.recommendations) else "1440p")
            else:
                col_render, col_export = st.columns(2)
                with col_render:
                    st.metric("Render Score", "95/100" if "High-end" in str(st.session_state.recommendations) else "75/100")
                with col_export:
                    st.metric("Export Speed", "Very Fast" if "High-end" in str(st.session_state.recommendations) else "Fast")
            
            # Export build
            if st.button("Export Build 📋", use_container_width=True):
                build_data = {
                    "components": st.session_state.recommendations,
                    "price_estimate": st.session_state.price_estimate,
                    "requirements": {
                        "use_case": use_case,
                        "budget": budget,
                        "preferences": preferences
                    }
                }
                st.download_button(
                    label="Download Build (JSON)",
                    data=json.dumps(build_data, indent=2),
                    file_name="my_pc_build.json",
                    mime="application/json",
                    use_container_width=True
                )
    
    # Footer
    st.markdown("---")
    st.markdown("""
    💡 **Note:** Prices and availability may vary. Always verify compatibility and current prices before making a purchase.
    """)

if __name__ == "__main__":
    main()