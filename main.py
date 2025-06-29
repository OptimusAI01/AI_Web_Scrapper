import streamlit as st
from scrap import scrap_website, extract_body_content, clean_body_contetn, split_dom_content
from parse import parse_with_ollama

st.title("Web Scraper")
url = st.text_input("Enter URL:")

if st.button("Scrape Site"):
    st.write("Scraping the Website !!!")
    
    result = scrap_website(url)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_contetn(body_content)
    st.session_state.dom_content = cleaned_content 
    
    with st.expander("View Dom Content"):
        st.text_area("Dom Content",cleaned_content,height=300)

if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe how to parse scraped content")
    
    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content")
            
            dom_batches = split_dom_content(st.session_state.dom_content)
            result = parse_with_ollama(dom_batches,parse_description)
            st.write(result)

