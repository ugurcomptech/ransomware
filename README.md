# Ransomware

Bu proje, dosyaları şifreleyen ve çözen bir ransomware uygulamasıdır.

**Uyarı: Bu kod örneği, yalnızca eğitim amaçlı olup, kötü niyetli kullanımı yasa dışıdır. Lütfen yasalar ve etik kurallar çerçevesinde kullanın.**

## Gereksinimler

- Python 3.x
- cryptography kütüphanesi

## Kurulum

1. Python 3.x'i [buradan](https://www.python.org/downloads/) indirin ve yükleyin.

2. Gerekli kütüphaneyi yüklemek için aşağıdaki komutu kullanın:

   ```shell
   pip install cryptography

3. ransomware.py dosyasını indirin veya kopyalayın.

## Kullanım
1. encryption_key.key adında bir şifreleme anahtarı oluşturmak için generate_key() fonksiyonunu çalıştırın.

2. Oluşturulan şifreleme anahtarını load_key() fonksiyonuyla yükleyin.

3. Şifrelemek veya çözmek istediğiniz dosyaların bulunduğu klasör yolunu belirtin ve encrypt_or_decrypt_files() fonksiyonunu çağırın. Örneğin:
   ```shell
   encrypt_or_decrypt_files("path/to/folder", key, encrypt=True)


5. Bu örnek, belirtilen klasördeki dosyaları şifreleyecektir. encrypt parametresini False olarak ayarlarsanız, dosyaları çözer.

## Notlar
Şifreleme anahtarı dosyası (encryption_key.key) oluşturulduktan sonra güvenli bir şekilde saklanmalıdır. Başkalarının erişimine kapalı ve kaybolmaması önemlidir.

Bu kod örneği sadece eğitim amaçlıdır ve kötü niyetli kullanımı önlemek için tasarlanmıştır. Lütfen yasalar ve etik kurallar çerçevesinde kullanın.

Dosyaları şifreleme veya çözme işlemi, encrypt_file() ve decrypt_file() fonksiyonlarında gerçekleştirilir. Bu fonksiyonları ihtiyaçlarınıza uygun şekilde düzenleyebilirsiniz.

## Lisans
Bu projenin lisansı MIT Lisansıdır. Daha fazla bilgi için LICENSE dosyasına bakın.
