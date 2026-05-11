import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px

# إعدادات الصفحة
st.set_page_config(page_title="Stock Analysis System", layout="wide")
st.title("📊 نظام تحليل بيانات سوق الأسهم")

# إدخال رمز السهم
symbol = st.text_input("أدخل رمز السهم (مثال: AAPL, MSFT, GOOGL):", "AAPL")

# جلب البيانات
ticker_data = yf.Ticker(symbol)
df = ticker_data.history(period="1mo")

if not df.empty:
    # عرض السعر الحالي
    current_price = df['Close'].iloc[-1]
    st.metric(label=f"السعر الحالي لشركة ({symbol})", value=f"${current_price:.2f}")

    # الرسم البياني
    st.subheader("📈 اتجاه السعر خلال آخر 30 يوم")
    fig = px.line(df, x=df.index, y='Close', labels={'Close': 'السعر', 'Date': 'التاريخ'})
    st.plotly_chart(fig, use_container_width=True)

    # عرض جدول البيانات
    st.subheader("📋 جدول البيانات التاريخية (آخر 10 أيام)")
    st.dataframe(df.tail(10))
else:
    st.error("⚠️ عذراً، هذا الرمز غير صحيح. يرجى التأكد من رمز الشركة.")