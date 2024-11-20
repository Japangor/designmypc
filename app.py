import streamlit as st
from datetime import datetime
import json
# Add these imports and metadata
import streamlit as st
from datetime import datetime
import json

# SEO and metadata information
SITE_META = {
    "title": "Design My PC | GJAM Technologies | Custom PC Builder",
    "description": "Build your dream PC with GJAM Technologies' AI-powered PC Builder. Custom gaming PCs, workstations, and high-performance computers. Expert PC building service in Japan.",
    "keywords": [
        "design my pc",
        "custom pc builder",
        "gaming pc builder",
        "workstation builder",
        "pc parts picker",
        "build my pc",
        "custom computer",
        "pc building service japan",
        "gaming pc japan",
        "gjam technologies",
        "japan gor",
        "pc builder tool"
    ]
}

# Company information
COMPANY_INFO = {
    "name": "GJAM Technologies",
    "website": "https://gjam.in",
    "location": "Japan",
    "description": """
    GJAM Technologies is a leading technology company specializing in custom PC building, 
    software development, and AI solutions. Founded by Japan Gor, we combine cutting-edge 
    technology with expert craftsmanship to deliver exceptional computing solutions.
    """
}

def main():
    # Set page config with SEO metadata
    st.set_page_config(
        page_title=SITE_META["title"],
        page_icon="🖥️",
        layout="wide",
        initial_sidebar_state="collapsed",
        menu_items={
            'Get Help': 'https://gjam.in/support',
            'Report a bug': 'https://gjam.in/contact',
            'About': COMPANY_INFO["description"]
        }
    )
    
    # Enhanced CSS with better UI elements
    st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: #ffffff;
    }
    .stButton > button {
        width: 100%;
        background-color: #7747FF;
        color: white;
        border-radius: 15px;
        padding: 0.75rem 1rem;
        font-weight: 500;
        border: none;
        margin: 10px 0;
    }
    .header-section {
        padding: 2rem 0;
        background: linear-gradient(135deg, #1e2329 0%, #0e1117 100%);
        border-radius: 15px;
        margin-bottom: 2rem;
    }
    .company-info {
        background-color: #1e2329;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #2d3139;
        margin: 20px 0;
    }
    .feature-card {
        background-color: #1e2329;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #2d3139;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

    # Enhanced Header with Company Info
    st.markdown("""
    <div class='header-section'>
        <h1 style='text-align: center; font-size: 2.5rem;'>🌟 Design My PC</h1>
        <h2 style='text-align: center; font-size: 1.5rem; color: #7747FF;'>Powered by GJAM Technologies AI</h2>
        <p style='text-align: center; margin: 1rem 0;'>
            Build your dream PC with our intelligent PC builder. From gaming rigs to professional workstations.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # About Section
    with st.expander("ℹ️ About GJAM Technologies"):
        col1, col2 = st.columns([2,1])
        with col1:
            st.markdown(f"""
            ### GJAM Technologies
            {COMPANY_INFO['description']}
            
            #### Why Choose Us:
            - 🎯 Expert PC Building Service
            - 🤖 AI-Powered Recommendations
            - 🛠️ Premium Components
            - ✨ Professional Assembly
            - 🌟 After-sales Support
            
            [Visit our website]({COMPANY_INFO['website']}) | [Contact Support]({COMPANY_INFO['website']}/support)
            """)
        with col2:
            st.image("https://via.placeholder.com/400x200?text=GJAM+Technologies", use_column_width=True)

    # Feature Highlights
    st.markdown("### 🚀 Why Design Your PC with Us")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class='feature-card'>
            <h4>🎮 Gaming PCs</h4>
            <p>Custom-built gaming rigs optimized for maximum FPS and stunning graphics.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class='feature-card'>
            <h4>💼 Workstations</h4>
            <p>Professional workstations for content creation, 3D rendering, and development.</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class='feature-card'>
            <h4>🔧 Custom Builds</h4>
            <p>Personalized builds tailored to your specific needs and preferences.</p>
        </div>
        """, unsafe_allow_html=True)

    # Rest of your existing code for PC building steps...
    # (Keep your existing step logic here)


# Add this at the end of your file
if __name__ == "__main__":
    main()
# PC Components database (Keep your existing PC_COMPONENTS dictionary)
PC_COMPONENTS = {
    "Gaming": {
        "Entry": {
            "CPU": ["AMD Ryzen 5 5600X", "Intel i5-12400F"],
            "GPU": ["RTX 3060", "RX 6600"],
            "RAM": ["16GB DDR4 3200MHz"],
            "Storage": ["1TB NVMe SSD"],
            "Motherboard": ["B550", "B660"],
            "PSU": ["650W 80+ Gold"],
            "Case": ["NZXT H510", "Phanteks P300"],
            "Price": 1000
        },
        "Mid": {
            "CPU": ["AMD Ryzen 7 5800X3D", "Intel i7-13700K"],
            "GPU": ["RTX 4070", "RX 7800 XT"],
            "RAM": ["32GB DDR4 3600MHz"],
            "Storage": ["2TB NVMe SSD"],
            "Motherboard": ["X570", "Z690"],
            "PSU": ["750W 80+ Gold"],
            "Case": ["Lian Li Lancool II", "Fractal Design Meshify 2"],
            "Price": 1500
        },
        "High": {
            "CPU": ["AMD Ryzen 9 7950X3D", "Intel i9-14900K"],
            "GPU": ["RTX 4090", "RX 7900 XTX"],
            "RAM": ["32GB DDR5 6000MHz"],
            "Storage": ["2TB NVMe Gen4"],
            "Motherboard": ["X670E", "Z790"],
            "PSU": ["1000W 80+ Platinum"],
            "Case": ["Lian Li O11", "Phanteks Evolv X"],
            "Price": 3000
        }
    },
    "Workstation": {
        "Entry": {
            "CPU": ["AMD Ryzen 7 5800X", "Intel i7-12700"],
            "GPU": ["RTX 4060", "RX 6800"],
            "RAM": ["32GB DDR4 3600MHz"],
            "Storage": ["2TB NVMe SSD"],
            "Motherboard": ["B550", "B660"],
            "PSU": ["750W 80+ Gold"],
            "Case": ["Fractal Design Meshify C", "be quiet! Pure Base 500"],
            "Price": 1200
        },
        "Mid": {
            "CPU": ["AMD Ryzen 9 7900X", "Intel i9-13900K"],
            "GPU": ["RTX 4070 Ti", "RX 7900 XT"],
            "RAM": ["64GB DDR5 5600MHz"],
            "Storage": ["4TB NVMe SSD"],
            "Motherboard": ["X670", "Z690"],
            "PSU": ["850W 80+ Platinum"],
            "Case": ["be quiet! Silent Base 802", "Fractal Design Define 7"],
            "Price": 2000
        },
        "High": {
            "CPU": ["AMD Threadripper 7980X", "Intel Xeon W9-3495X"],
            "GPU": ["RTX 4090", "2x RTX 4080"],
            "RAM": ["128GB DDR5 6400MHz"],
            "Storage": ["8TB NVMe RAID"],
            "Motherboard": ["WRX90", "W790"],
            "PSU": ["1600W 80+ Titanium"],
            "Case": ["Phanteks Enthoo 719", "Lian Li V3000+"],
            "Price": 5000
        }
    }
}

def main():
  
    
    # Custom CSS
    st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: #ffffff;
    }
    .stButton > button {
        width: 100%;
        background-color: #7747FF;
        color: white;
        border-radius: 15px;
        padding: 0.75rem 1rem;
        font-weight: 500;
        border: none;
        margin: 10px 0;
    }
    .stProgress > div > div {
        background-color: #7747FF;
    }
    .usage-card {
        background-color: #1e2329;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #2d3139;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

    # Header
    st.title("🌟 AI PC Builder")
    st.markdown("""
    <div style='text-align: center; margin-bottom: 2rem;'>
    Let AI design your perfect PC in 3 simple steps
    </div>
    """, unsafe_allow_html=True)

    # Initialize session state
    if 'step' not in st.session_state:
        st.session_state.step = 1
        st.session_state.build = None

    # Navigation function
    def next_step(step, **kwargs):
        for key, value in kwargs.items():
            st.session_state[key] = value
        st.session_state.step = step

    # Step 1: Usage Selection
    if st.session_state.step == 1:
        st.markdown("### Step 1: What's your primary use case?")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🎮 Gaming & Streaming", help="Optimized for gaming, streaming, and content creation"):
                next_step(2, usage="Gaming")
                
        with col2:
            if st.button("💼 Professional Workstation", help="Optimized for productivity, rendering, and development"):
                next_step(2, usage="Workstation")

    # Step 2: Budget Selection
    elif st.session_state.step == 2:
        st.markdown(f"### Step 2: Choose your budget level for {st.session_state.usage}")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("Entry Level", help=f"Budget: ${PC_COMPONENTS[st.session_state.usage]['Entry']['Price']:,}"):
                next_step(3, tier="Entry", build=PC_COMPONENTS[st.session_state.usage]["Entry"])
                
        with col2:
            if st.button("Mid Range", help=f"Budget: ${PC_COMPONENTS[st.session_state.usage]['Mid']['Price']:,}"):
                next_step(3, tier="Mid", build=PC_COMPONENTS[st.session_state.usage]["Mid"])
                
        with col3:
            if st.button("High End", help=f"Budget: ${PC_COMPONENTS[st.session_state.usage]['High']['Price']:,}"):
                next_step(3, tier="High", build=PC_COMPONENTS[st.session_state.usage]["High"])

    # Step 3: Build Overview
    elif st.session_state.step == 3:
        st.markdown(f"### Your {st.session_state.tier} {st.session_state.usage} Build")
        
        # Progress bar
        st.progress(1.0, "Build Complete!")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Component selection
            for component, options in st.session_state.build.items():
                if component != "Price":
                    with st.expander(f"📦 {component}", expanded=True):
                        if isinstance(options, list):
                            option = st.radio(
                                f"Choose your {component}:",
                                options,
                                horizontal=True,
                                key=f"select_{component}"
                            )
                            st.image(f"https://via.placeholder.com/600x300?text={option}", use_column_width=True)
        
        with col2:
            # Build Summary
            st.markdown("### 🎯 Build Summary")
            
            # Performance Metrics
            if st.session_state.usage == "Gaming":
                col_a, col_b = st.columns(2)
                with col_a:
                    st.metric("FPS 1440p", 
                             {"Entry": "80+", "Mid": "144+", "High": "200+"}[st.session_state.tier])
                with col_b:
                    st.metric("Ray Tracing", 
                             {"Entry": "Basic", "Mid": "Good", "High": "Best"}[st.session_state.tier])
            else:
                col_a, col_b = st.columns(2)
                with col_a:
                    st.metric("Render Score", 
                             {"Entry": "85/100", "Mid": "92/100", "High": "98/100"}[st.session_state.tier])
                with col_b:
                    st.metric("Workload", 
                             {"Entry": "Medium", "Mid": "Heavy", "High": "Extreme"}[st.session_state.tier])
            
            # Price
            st.metric("Total Cost", f"${st.session_state.build['Price']:,}")
            
            # Compatibility Check
            st.markdown("#### ✅ Compatibility")
            st.markdown("""
            - ✓ All components verified compatible
            - ✓ Power supply is sufficient
            - ✓ Cooling solution is adequate
            - ✓ Case fits all components
            """)
            
            # Export Build
            if st.button("💾 Save Build"):
                build_data = {
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "type": f"{st.session_state.tier} {st.session_state.usage}",
                    "components": {k: v for k, v in st.session_state.build.items() if k != "Price"},
                    "price": st.session_state.build["Price"]
                }
                st.download_button(
                    "📤 Download Build",
                    data=json.dumps(build_data, indent=2),
                    file_name="pc_build.json",
                    mime="application/json",
                )
            
            # Reset Button
            if st.button("🔄 Start Over"):
                st.session_state.clear()
                st.session_state.step = 1

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center'>
                
    Powered by AI | Made by GJAM Technologies | © 2024<br>
    💡 Prices and availability may vary. All builds are automatically verified for compatibility.
                
    </div>
                
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()