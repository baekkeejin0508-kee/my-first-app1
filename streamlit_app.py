 import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# 페이지 기본 설정
st.set_page_config(
    page_title="Streamlit 요소 예시",
    page_icon="🎨",
    layout="wide"
)

# ==================== 제목 & 텍스트 요소 ====================
st.title("🎨 Streamlit 주요 요소 가이드")
st.markdown("---")

st.header("📝 1. 텍스트 요소")
st.subheader("기본 텍스트 표시")
st.write("이것은 `st.write()`를 사용한 텍스트입니다.")
st.text("이것은 `st.text()` - 고정 너비 폰트입니다.")

st.subheader("마크다운 형식")
st.markdown("""
- **굵은 텍스트**: `**텍스트**`
- *이탤릭 텍스트*: `*텍스트*`
- ~~취소선~~: `~~텍스트~~`
- `코드`: `` `코드` ``
- [링크](https://streamlit.io)
""")

st.subheader("코드 표시")
st.code("""
def hello_world():
    print("안녕하세요, Streamlit!")
    
hello_world()
""", language="python")

st.markdown("---")

# ==================== 입력 위젯 ====================
st.header("🎮 2. 입력 위젯 (입력 요소)")

col1, col2 = st.columns(2)

with col1:
    st.subheader("텍스트 입력")
    name = st.text_input("이름을 입력하세요:", value="사용자")
    comment = st.text_area("의견을 남겨주세요:", height=100)

with col2:
    st.subheader("숫자 입력")
    age = st.number_input("나이:", min_value=0, max_value=120, value=25)
    score = st.slider("만족도 (0-100):", 0, 100, 50)

st.subheader("선택 입력")
col1, col2, col3 = st.columns(3)

with col1:
    st.write("체크박스")
    agree = st.checkbox("동의합니다")

with col2:
    st.write("라디오 버튼")
    option = st.radio("선택하세요:", ("옵션1", "옵션2", "옵션3"))

with col3:
    st.write("셀렉트박스")
    selected = st.selectbox("고르세요:", ["선택1", "선택2", "선택3"])

st.subheader("다중 선택 & 날짜")
col1, col2 = st.columns(2)

with col1:
    multi = st.multiselect("복수 선택:", ["A", "B", "C", "D"], default=["A"])

with col2:
    date = st.date_input("날짜 선택:", datetime.now())

st.subheader("파일 업로드 & 버튼")
col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader("파일을 선택하세요:")
    if uploaded_file:
        st.write(f"파일명: {uploaded_file.name}")

with col2:
    if st.button("클릭 버튼 🔘"):
        st.success("버튼이 클릭되었습니다!")

st.markdown("---")

# ==================== 데이터 표시 ====================
st.header("📊 3. 데이터 표시")

# 샘플 데이터 생성
sample_data = pd.DataFrame({
    "이름": ["Alice", "Bob", "Charlie", "Diana"],
    "수학": [85, 92, 78, 95],
    "영어": [90, 88, 85, 92],
    "과학": [88, 85, 90, 94]
})

st.subheader("데이터프레임")
st.dataframe(sample_data, use_container_width=True)

st.subheader("정적 테이블")
st.table(sample_data)

st.subheader("메트릭 표시")
col1, col2, col3, col4 = st.columns(4)
col1.metric("평균 수학", "87.5", "+2.3%")
col2.metric("평균 영어", "88.8", "-1.1%")
col3.metric("평균 과학", "89.3", "+3.5%")
col4.metric("전체 평균", "88.5", "+1.6%")

st.markdown("---")

# ==================== 차트 & 시각화 ====================
st.header("📈 4. 차트 & 시각화")

# 시계열 데이터
dates = pd.date_range('2024-01-01', periods=30)
chart_data = pd.DataFrame({
    "날짜": dates,
    "판매량": np.random.randint(50, 200, 30),
    "방문자": np.random.randint(100, 500, 30)
})

col1, col2 = st.columns(2)

with col1:
    st.subheader("라인 차트")
    st.line_chart(chart_data.set_index("날짜")["판매량"])

with col2:
    st.subheader("바 차트")
    st.bar_chart(chart_data.set_index("날짜")["방문자"])

col1, col2 = st.columns(2)

with col1:
    st.subheader("에어리어 차트")
    area_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['A', 'B', 'C']
    )
    st.area_chart(area_data)

with col2:
    st.subheader("스캐터 차트")
    scatter_data = pd.DataFrame(
        np.random.randn(100, 2),
        columns=['x', 'y']
    )
    st.scatter_chart(scatter_data)

st.markdown("---")

# ==================== 레이아웃 요소 ====================
st.header("🎯 5. 레이아웃 요소")

st.subheader("탭 (Tabs)")
tab1, tab2, tab3 = st.tabs(["탭1", "탭2", "탭3"])

with tab1:
    st.write("이것은 탭 1의 내용입니다.")

with tab2:
    st.write("이것은 탭 2의 내용입니다.")

with tab3:
    st.write("이것은 탭 3의 내용입니다.")

st.subheader("확장 컨테이너 (Expander)")
with st.expander("자세히 보기"):
    st.write("이것은 숨겨졌던 내용입니다.")
    st.write("확장 버튼을 클릭하면 나타나요!")

st.markdown("---")

# ==================== 상태 메시지 ====================
st.header("💬 6. 상태 & 알림 메시지")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("✅ 성공!")

with col2:
    st.info("ℹ️ 정보")

with col3:
    st.warning("⚠️ 경고")

col1, col2 = st.columns(2)

with col1:
    st.error("❌ 오류 발생")

with col2:
    st.caption("캡션 텍스트 - 작은 크기")

st.markdown("---")

# ==================== 사이드바 ====================
st.header("🎛️ 7. 사이드바 (Sidebar)")
st.write("➡️ 왼쪽 사이드바를 확인해보세요!")

with st.sidebar:
    st.header("⚙️ 설정")
    sidebar_name = st.text_input("사용자명:", "사용자")
    sidebar_theme = st.radio("테마:", ["밝음", "어두움"])
    
    if st.sidebar.button("저장"):
        st.sidebar.success("설정이 저장되었습니다!")

# ==================== 세션 상태 ====================
st.header("💾 8. 세션 상태 (Session State)")

if "counter" not in st.session_state:
    st.session_state.counter = 0

col1, col2 = st.columns(2)

with col1:
    if st.button("증가 +"):
        st.session_state.counter += 1

with col2:
    if st.button("감소 -"):
        st.session_state.counter -= 1

st.write(f"현재 카운터: **{st.session_state.counter}**")

st.markdown("---")

# ==================== 최종 정보 ====================
st.header("📚 Streamlit 요소 정리")
st.markdown("""
### 주요 요소 카테고리:
1. **텍스트 요소**: title(), header(), subheader(), write(), text(), markdown(), code()
2. **입력 위젯**: button(), checkbox(), radio(), selectbox(), multiselect(), slider(), text_input(), text_area(), number_input(), date_input(), time_input(), file_uploader()
3. **데이터 표시**: dataframe(), table(), metric()
4. **시각화**: line_chart(), bar_chart(), area_chart(), scatter_chart()
5. **레이아웃**: columns(), expander(), tabs(), container(), sidebar
6. **상태**: success(), info(), warning(), error(), session_state
7. **미디어**: image(), audio(), video()

더 알아보기: [Streamlit Documentation](https://docs.streamlit.io)
""")
