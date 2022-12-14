from student import SinhVien
import pickle
import os
#Luu tru
def luu_sinhvien(thumuc: str, ten_taptin: str, objs: list[SinhVien]):
    try:
        with open (os.path.join(thumuc, ten_taptin), 'wb') as f:
            pickle.dump(objs,f)
        print("Kết thúc ghi tập tin")
    except Exception as e:
        print("Lỗi khi ghi tập tin", e)
        
#Doc tap tin
def doc_sinhvien(thumuc: str, ten_taptin: str)-> list[SinhVien]:
    try:
        with open (os.path.join(thumuc, ten_taptin), 'rb') as f:
            sv = pickle.load(f)
        return sv
    except Exception as e:
        return None
    
def in_list_sinh_vien(s: list[SinhVien]):
    for i in s:
        print(i)
        
def main():
    path = 'D:\\data'
    filename = 'sinhvien1.dat'
    sv = [SinhVien('Lê Ngọc Thuận', 2004, 10.0),
          SinhVien('Lê Quý Minh Quang', 2004, 10.0),
          SinhVien('Lê Minh Quý Quang', 2004, 10.0)]
    luu_sinhvien(path,filename,sv)
    noidung = doc_sinhvien(path,filename)
    print(noidung)
    in_list_sinh_vien(noidung)
    print('Kết thúc chương trình')
if __name__ == "__main__":
    main()