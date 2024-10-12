#kullanıcıdan alınan parola 8 karakterden az ise parolanız 8 karakter olmalıdır uyarsıı verren parola 8 karakterden uzunsa parolanız aktif edilmiştir yazan program
parola=input("parola giriniz")
z=len(parola)
if(z<8):
    print("parolanız 8 karakterden uzun olmalıdır")
else:
    print("parolanız başarı ile kaydedilmiştir")