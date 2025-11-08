import streamlit as st
from sympy import symbols, Matrix, simplify, Rational, latex

st.set_page_config(page_title="Hình học không gian", layout="wide")
st.title("📐 Hình học không gian: A, B, C, D")

st.markdown("### 🔢 Nhập tọa độ các điểm:")

def nhap_diem(ten):
    col1, col2, col3 = st.columns(3)
    with col1:
        x = st.number_input(f"{ten} - x", value=0.0, key=f"{ten}_x")
    with col2:
        y = st.number_input(f"{ten} - y", value=0.0, key=f"{ten}_y")
    with col3:
        z = st.number_input(f"{ten} - z", value=0.0, key=f"{ten}_z")
    return Matrix([x, y, z])

def hien_toa_do(vec):
    x, y, z = [Rational(v).limit_denominator() for v in vec]
    return f"({latex(x)}; {latex(y)}; {latex(z)})"

def hien_so(expr):
    val = Rational(expr).limit_denominator()
    return latex(val)

A = nhap_diem("A")
B = nhap_diem("B")
C = nhap_diem("C")
D = nhap_diem("D")

if st.button("🧠 Tính toán"):
    AB = B - A
    AC = C - A
    AD = D - A

    st.subheader("✅ Kết quả:")

    st.write("1. Trung điểm I của AB:")
    st.latex(hien_toa_do((A + B)/2))

    st.write("2. Trọng tâm tam giác ABC:")
    st.latex(hien_toa_do((A + B + C)/3))

    st.write("3. Điểm M để ABCM là hình bình hành:")
    st.latex(hien_toa_do(A + (C - B)))

    st.write("4. A, B, C thẳng hàng?")
    thang_hang = AB.cross(AC).is_zero
    st.write(thang_hang)

    st.write("5. A, B, C, D đồng phẳng?")
    if thang_hang:
        st.write("Không xác định (A, B, C thẳng hàng)")
    else:
        tich_hon_hop = AB.cross(AC).dot(AD)
        st.write(tich_hon_hop == 0)

    st.write("6. Tích vô hướng \\( \\overrightarrow{AB} \\cdot \\overrightarrow{AC} \\):")
    st.latex(hien_so(AB.dot(AC)))

    st.write("7. Tích có hướng \\( \\overrightarrow{AB} \\times \\overrightarrow{AC} \\):")
    st.latex(hien_toa_do(AB.cross(AC)))

    st.write("8. \\( \\cos(\\overrightarrow{AB}, \\overrightarrow{AC}) \\):")
    cos_theta = simplify(AB.dot(AC)/(AB.norm()*AC.norm()))
    st.latex(hien_so(cos_theta))

    # Phương trình mặt phẳng (ABC)
    if not thang_hang:
        n = AB.cross(AC)
        x, y, z = symbols('x y z')
        d = -n.dot(A)
        pt_mat_phang = simplify(n[0]*x + n[1]*y + n[2]*z + d)
        st.write("9. Phương trình mặt phẳng (ABC):")
        st.latex(latex(pt_mat_phang) + " = 0")
    else:
        st.write("9. Phương trình mặt phẳng (ABC): Không xác định (A, B, C thẳng hàng)")

    # Khoảng cách từ D đến mặt phẳng (ABC)
    if not thang_hang:
        khoang_cach_D = simplify(abs(n.dot(D - A)) / n.norm())
        st.write("10. Khoảng cách từ D đến mặt phẳng (ABC):")
        st.latex(hien_so(khoang_cach_D))
    else:
        st.write("10. Khoảng cách từ D đến mặt phẳng (ABC): Không xác định")

    # Khoảng cách giữa AB và CD
    n2 = AB.cross(D - C)
    if n2.norm() == 0:
        st.write("11. Khoảng cách giữa AB và CD: 0 (song song hoặc trùng nhau)")
    else:
        kc_duong_thang = simplify(abs((C - A).dot(n2)) / n2.norm())
        st.write("11. Khoảng cách giữa AB và CD:")
        st.latex(hien_so(kc_duong_thang))
