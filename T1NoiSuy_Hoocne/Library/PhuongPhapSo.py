import sys
MyPATH_LIB = __file__.split('\\')[:-3]
MyPATH_LIB.append('zLibrary')
sys.path.append('\\'.join(MyPATH_LIB))
print('___✅ Thêm thư viện Phương pháp số___')
