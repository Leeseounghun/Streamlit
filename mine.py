import streamlit as st
import folium
import pandas as pd

# 페이지 선언
def main_page():
    
    st.image("war.jpg", use_column_width=True)
    st.markdown("# 6.25 정보")
    st.sidebar.title('6.25 정보')

    st.markdown("### 6.25 정보 페이지에 오신 것을 환영합니다!")
    st.markdown("""6.25 전쟁(한국 전쟁)은 1950년 6월 25일부터 1953년 7월 27일까지 한반도에서 벌어진 전쟁입니다.""")

    st.markdown("""이 전쟁은 3년 동안 진행되었으며, 휴전 합의로 끝났습니다.""")

    st.markdown("""이 페이지의 좌측 사이드바에서 로그인 페이지로 이동할 수 있습니다.""")

def login_page():
    st.header('로그인')
    st.sidebar.title('로그인')

    radio_choice = st.radio("성별을 선택하세요:", ("남성", "여성"))
    
    age = st.slider('나이가 어떻게 되세요 ? ', 0, 120, 25)
    st.write(age, '세')

    selectbox_choice = st.selectbox("국가를 선택하세요:", ["한국", "미국", "영국", "캐나다", "호주", "뉴질랜드", "필리핀",
                                                   "터키", "태국", "그리스", "네덜란드", "벨기에", "룩셈부르크"])

    # 리스트로 선택 가능, ', '.join(options) -> 선택한 게 옆으로 보임
    options = ["검색", "지인소개", "광고"]
    multiselect_choice = st.multiselect("방문 경로를 입력해주세요:", options, default=["검색"])
    
    checkbox_checked = st.checkbox("개인정보 수집에 동의합니다.")

    on = st.toggle('국가유공자이신가요?')
    if on:
        st.write('나라 지켜주셔서 감사합니다!')
    if checkbox_checked:
        st.write("개인정보 수집에 동의했습니다.")
        
    button_clicked = st.button("로그인")    
    
    if button_clicked:
        st.write("로그인 확인!")
        st.write("참여국 별 사망자 수 정보입니다")
        death_toll_page()


    

def death_toll_page():
    st.header('참여국 별 사망자 수')
    st.sidebar.title('참여국 별 사망자 수')
    
    map_data = pd.DataFrame({
        'lat': [35.9078, 38.9072, 55.05, 59.72, -24.88, -42.92, 12.36, 38.916, 15.58, 39.46, 52.21, 50.95, 49.61],
        'lon': [127.7669, -101, -2.87, -110.9, 133.6, 170.9, 122.88, 35.18, 100.74, 22.39, 5.70, 4.37, 6.12],
        'name': ['한국', '미국', '영국', '캐나다', '호주', '뉴질랜드', '필리핀', '터키', '태국', '그리스', '네덜란드', '벨기에', '룩셈부르크'],
        'value': [148600, 30000, 1000, 5000, 1000, 300, 1000, 7000, 2000, 200, 100, 100, 2] 
    })

    my_map = folium.Map(location=[map_data['lat'].mean(), map_data['lon'].mean()], zoom_start=2)

    for index, row in map_data.iterrows():
        folium.CircleMarker(
            location=[row['lat'], row['lon']],
            radius=row['value'] / 7500,
            color='pink',
            fill=True,
            fill_opacity=1.0
        ).add_to(my_map)

        # Popup을 사용하여 나라 이름을 표시 (bold)
        folium.Marker(
            location=[row['lat'], row['lon']],
            popup=f"<b>{row['name']}</b>",
            icon=folium.DivIcon(html=f"<div>{row['name']} {row['value']}</div>"),
        ).add_to(my_map)

    st.caption("참전국 별 사망자 수")

    # HTML을 통해 지도를 출력합니다.
    st.components.v1.html(my_map._repr_html_(), width=800, height=600)

# 페이지 딕셔너리 선언
page_functions = {
    '6.25 정보': main_page,
    '로그인': login_page
}


def main():
    # 사이드 바에서 selectbox 선언 & 선택 결과 저장
    selected_page = st.sidebar.selectbox('페이지 선택', list(page_functions.keys()))

    # 선택된 페이지 함수 호출
    page_functions[selected_page]()

if __name__ == "__main__":
    main()

    
    
    
    
    
# 실행 - streamlit run mine.py

# python -m streamlit run streamlit\mine.py