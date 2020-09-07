import pandas as pd 
import streamlit as st

def main():
    st.title('Using Pandas with Streamlit')
    file_uploader = st.file_uploader('Upload your file', type="csv")
    if file_uploader is not None:
        slider = st.slider('Valores', 1, 100)
        df = pd.read_csv(file_uploader)
        st.dataframe(df.head(slider))
        st.write(df.columns)
        st.table(df.groupby('species')['petal_width'].mean())
        # st.markdown('Table')
        # st.table(df.head(slider))


if __name__ == '__main__':
    main()

