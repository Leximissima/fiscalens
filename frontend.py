import streamlit as st


def financial_statements():
    st.title('FiscalLense')
    st.header("Be as smart as a financial analyst \n", divider="gray")

    st.write("Upload your financial statements to get a summary of the financial health of your company.")

    if "chat_history" not in st.session_state:
        st.session_state['chat_history'] = []

    with st.form("llm-form"):
        uploaded_files = st.file_uploader(
            "Choose a CSV file", accept_multiple_files=True
        )
        for uploaded_file in uploaded_files:
            bytes_data = uploaded_file.read()
            st.write("filename:", uploaded_file.name)
            st.write(bytes_data)
        
        submit = st.form_submit_button("Submit")
   
    # statement_type = st.selectbox("Select financial statement type:", ["Income Statement", "Balance Sheet", "Cash Flow"])

    # col1, col2 = st.columns(2)

    # with col1:
    #     period = st.selectbox("Select period:", ["Annual", "Quarterly"]).lower()

    # with col2:
    #     limit = st.number_input("Number of past financial statements to analyze:", min_value=1, max_value=10, value=4)
    

    # ticker = st.text_input("Please enter the company ticker:")

    # if st.button('Run'):
    #     if ticker:
    #         ticker = ticker.upper()
    #         financial_statements = "get_financial_statements"

    #         with st.expander("View Financial Statements"):
    #             st.dataframe(financial_statements)

    #         financial_summary = "generate_financial_summary(financial_statements, statement_type)"
    #         st.write(f'Summary for ticker:\n financial_summary\n')

def main():
    st.sidebar.title('FiscalLense')
    
    app_mode = st.sidebar.selectbox("Choose your AI assistant:",
        ["Financial Statements"])
    if app_mode == 'Financial Statements':
        financial_statements()


if __name__ == '__main__':
    main()