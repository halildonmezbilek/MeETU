## Entry 2766

Question: What is Host Trafic Log? (In Turkish)
Answer: 

English version will be available soon.
24 Ekim 2007 tarih ve 26680 sayılı Resmi Gazete'de yayınlanan yönetmeliğe göre,
"Yer sağlayıcı trafik bilgisi, İnternet ortamındaki her türlü yer sağlamaya ilişkin olarak; kaynak IP adresi, hedef IP adresi, bağlantı tarih-saat bilgisi, istenen sayfa adresi, işlem bilgisi (GET, POST komut detayları) ve sonuç bilgisi gibi bilgileri ifade etmektedir."
Tanımlanan bu bilgiye, bir hukuksal incelemede kullanılmak üzere yer sağlayıcılık faaliyetleri kapsamındaki bir faaliyetin kim tarafından yapıldığının tespiti için ihtiyaç duyulmaktadır.
l) Örnek "http" logu:
Aşağıda yer sağlayıcı faaliyet kapsamında bir web sayfasının bulunduğu sunucunun ilgili örnek trafik logu (http logu) gösterilmiştir. Bu log, "apache" web sunucu yazılımının ürettiği bir log örneğidir. Birimlerde kullanılan farklı web sunucu yazılımları için, yazılımların belgelerine başvurulması ve uygun log tutulması için hangi işlemlerin yapılmasının gerekli olduğunun öğrenilmesi gerekmektedir.
144.122.222.234 - - [21/Mar/2008:14:58:01 -0200] "GET 'data/liste.html HTTP/1.1" 200"1 73372 "-" "Mozilla/5.0 (XII: U; Lınux i686; en-L'S; rv:1.8.1.12) Gecko/20080129 Iceweasel/2.0.0.12(Debian-2.0.0.12-Oetchl)"

Yukarıdaki örnekte yer alan bilgi alanları, kanunda belirtilen başlıklarla aşağıdaki şekilde ilişkilendirilmiştir:
Kaynak IP adresi : 144.122.222.234 Hedef ip adresi: Bu kayıtta bulunmamaktadır" Bağlantı tarih-saat bilgisi: [21/Mar/2008:14:58:01 -0200] İstenen sayfa adresi: data/liste.html İşlem bilgisi (GET komut detayı) : GET 'data/liste.htmi HTTP/1.1 Sonuç bilgisi: 200

2) Örnek e-posta logu:
"sendmail" e-posta sunucu yazılımının ürettiği log dosyasının örneği aşağıda verilmiştir. Tutulan log bilgisinde, "to", "from" ve "relay" bilgilerinin bulunması gereklidir. Kullanılan e-posta yazılımının log formatı, istenen bilgileri bir veya birden fazla satır halinde verebilir.
Mar 25 10:20:02 mailhost sendmail[9516]: m2Q8K2e2009516:  from=<bogususerbogus.com>, size=2291, class=0, nrcpts=1,  msgid=<00b101c88f1a$407a7cf0$>, proto=ESMTP, daemon=MTA, relay=boguspc.bogus.com [192.168.1.1] Mar 25 10:20:03 mailhost sendmail[9550]: m2Q8K2e1009516:  to=<bogus2userbogus2.com>, delay=00:00:01, xdelay=00:00:00,  mailer=esmtp, pri=122357, relay=mx.bogus2.com. [192.168.1.2], dsn=2.0.0,  stat=Sent ( Queued mail for delivery)

Yukarıdaki örnekte yer alan bilgi alanları, kanunda belirtilen başlıklarla aşağıdaki şekilde ilişkilendirilmiştir:
Bağlantı tarih-saat bilgisi: "Mar 25 10:20:03" Gönderici: bogususerbogus.com Kaynak IP adresi: 192.168.1.1 Hedef IP adresi: 192.168.1.2 Alıcı: bogus2userbogus2.com Sonuç bilgisi: sent

3) Örnek ftp logu:
"proftpd" ftp sunucu yazılımının ürettiği log dosyasının örneği aşağıda verilmiştir. Tutulan log bilgisinde, bağlantı yapan bilgisayarın adresi, hedef dosya ve kullanıcı adı bilgileri bulunmalıdır.
Tue Mar 25 16:39:48 2008 0 bogus.com 528 /ftp/pub/IMPORTANT-WARNING.txt b _ o r anonim ftp 1 * c

Yukarıdaki örnekte yer alan bilgi alanları, kanunda belirtilen başlıklarla aşağıdaki şekilde ilişkilendirilmiştir:
Bağlantı tarih-saat bilgisi: "Tue Mar 25 16:39:48 2008"  Kaynak Adres: "bogus.com"  İstenen dosya: "ftp/pub/IMPORTANT-WARNING.txt"  Kullanıcı adı: "anonim"

Birimler, yer sağlayıcı faaliyetleri kapsamında verdikleri servislerin ürettiği logları inceleyip, sahip oldukları sistemlerde verdikleri servislerin yarattığı trafik loglarını yönetmelikte tarif edildiği şekilde (zaman damgası ile birlikte) kayıt altına almak, bu logları, gizliliğini sağlayarak arşivlemekle yükümlüdür.



Link: https://faq.cc.metu.edu.tr/faq/what-host-trafic-log-turkish

---

## Entry 2767

Question: What is Internal IP Distribution Log? (In Turkish)
Answer: 

English version will be available soon.
1 Kasım 2007 tarih ve 26687 sayılı Resmi Gazete'de yayınlanan yönetmelikteki tanıma göre, "İç IP Dağıtım Logları, kendi iç ağlarında dağıtılan IP adres bilgilerini, kullanıma başlama ve bitiş tarih ve saatini ve bu IP adreslerini kullanan bilgisayarların tekil ağ cihaz numarasını (MAC adresi) gösteren bilgileri" ifade etmektedir.
Bu ifadede daha çok NAT (Network Adress Translation) gibi dinamik olarak IP alan sistemler tanımlanmış olsa da, genel olarak bir IP adresinin hangi bilgisayar tarafından kullanıldığının ve bu bilgiden yola çıkarak kullanıcı tespitinin yapılması amaçlanmaktadır.
Bu nedenle, birimlerde kişisel ve ortak kullanımda olan bilgisayarların IP adreslerinin bağlı olduğu MAC adreslerini kullanan kullanıcıların da kayıt altına alınması gereklidir.
Kendi yapılarında NAT gibi dinamik olarak IP dağıtan birimler, hangi IP adresinin hangi MAC adresli bilgisayar ve kim tarafından hangi zaman diliminde kullanıldığının tespitini sağlayacak bilgileri elektronik ortamda tutmakla yükümlüdür.
Kendi yapılarında dinamik olmayan, her bilgisayara ait sabit olarak tanımlanmış IP adresi kullanan birimler, hangi MAC adresli bilgisayara hangi IP adresinin verildiğini, kimin kullanımına tahsis edildiğini, kullanıma başlama-bitiş tarih ve saatini benzer şekilde elektronik ortamda kayıt altına almak zorundadır.



Link: https://faq.cc.metu.edu.tr/faq/what-internal-ip-distribution-log-turkish

---

## Entry 2768

Question: What is phishing?
Answer: Phishing, an expression derived from "password fishing", is an illegal way of collecting personal information such as passwords, bank or credit card account details etc. by sending misleading and fraudulent e-mails.
Due to security reasons, METU-CC never sends any e-mails for the need to update user information such as account name, password etc.
How to discover phishing
It is technically possible to arrange the "From" line in a manner to mislead users on an e-mail. It is crucial not to open address links on e-mail messages demanding your personal information updates or other similar topics.
Never click on the link addresses given in the e-mail that asks you to update your personal information like credit card details, passwords etc. Due to security reasons, establishments that provide services on the internet such as banks, brokerage houses, internet service providers etc. never send their user info update requirements by e-mail. Upon receiving such e-mail, contact the related corporate and confirm whether the contents of the e-mail you received are actually valid.
Lately there has been observed an increase in the number of e-mail sent to mislead users and get their personal information. As time progresses it becomes harder and harder to detect such bogus e-mails. Therefore, in case of doubt, be sure whether the e-mail has been sent specifically to you or not. Check the "To" section if there is only your e-mail address written or the message is sent under a general user name as a bulk. If the e-mail has not been sent specifically to you and the content is suspicious, you can regard that message as fake or spam. Suspicious contents can be as follows:
Looking for candidates to work for high pay.
I'm the son of the richest tribes chief of Africa, have inherited a large sum, could you help out?
Congratulations, you've earned the biggest prize, click on the link to accept.
The fake web pages given on the bogus e-mails have some various characteristics in common.

Generally the pictures are low quality.
When you check the address line, you can observe that the connection made is not to the web page intended but to some other address or maybe directly to an IP number.
Some bogus e-mails are also sent to collect e-mail addresses. Avoid e-mail messages with instructions like "click on the attached file in order to ...".
Do not click on message lines like "if you do not wish to receive similar e-mails click here to unsubscribe" in order not to be flooded with spam e-mail.
There are also some e-mail messages that can be for real, but most probably may be bogus, which arouse attention of users with their social content. Such e-mails cause loss of time and resources. Topics like charity donation, help for an ill child or the need for a wheel chair, the need of the e-mail to be forwarded to as many people as you can etc. are all examples of bogus e-mail.
Phishing e-mail examples

 -------- Original Message -------- 
From: XXXX Bank To: metuusermetu.edu.tr Date: Sun, 16 Jan 2011 07:21:55 +0200 Subject: E-Mail/Your GSM Number
Dear XXXX Bank Customer,
Any information you wish to get at goes through our E-mail / SMS services.
XXXX Bank Internet Banking users should indicate their E-mail account / GSM number along with their customer information so as to receive alerts and announcements. Thanks to this warning system any transactions on your account will be conveyed on you as a daily or instantaneous report according to your instruction. Furthermore if you wish, you may have information on economy, daily info, reminders, and other similar detail sent to your cellular or e-mail address at no cost.
Please indicate your e-mail account / GSM number along with your personal information by clicking here.
After you enter the Internet Banking site, click on E-Mail / SMS Services by selecting the services you wish to get you can start making use of our services.
CLICK FOR INTERACTIVE BANKING > http://www.XXXXbank_net.com
Best regards,
XXXX Bank
-------- Original Message -------- 
From: XXXXbankXXXXbank.com.tr (eychennebigfoot.com) To:metuusermetu.edu.tr Date: Tue, 18 Jan 2011 10:40:53 -0400 Subject: Dear Customer
Dear Customer,
We have detected that there has been trials to get to your account from different IP addresses. If you have tried to access your bank account during a travel this can be accounted for the above activity. However, if this is not the case, we strongly recommend that you apply to your bank at your earliest convenience in order to check all your account information.
http://www.XXXXbank_net.com
Thank you for your patience.
Best regards,
XXXX Bank  
-------- Original Message -------- From:securitymetu.edu.tr To:metuusermetu.edu.tr Date: Tue, 7 Feb 2011 17:18:12 +0900 Subject: Account Alert
Dear Valued Member,
According to our terms of services, you will have to confirm your e-mail by the following link, or your account will be suspended within 24 hours for security reasons.
metuusermetu.edu.tr/confirm.php?account=metu.edu.tr
After following the instructions in the sheet, your account will not be interrupted and will continue as normal.
Thanks for your attention to this request. We apologize for any inconvenience.
Sincerely,
METU Security Department


Link: https://faq.cc.metu.edu.tr/faq/what-phishing

---

## Entry 2769

Question: What is Time Stamp, why is it have to be used? (In Turkish)
Answer: 

English version will be available soon.
Zaman damgası nedir?
Zaman damgası, elektronik ortamda log, doküman ve sözleşme gibi elektronik verilerin, belirli bir zamandan önce var olduğunu kanıtlamak için kullanılır. Mesela bir log dosyasının, kayıt altına alındıgı tarihte orjinal haliyle var oldugunu, sonradan değiştirilmediğini ispatlamak amacıyla zaman damgasından yararlanılabilir.
Niçin Kullanılması Gerekmektedir?
30 Kasım 2007 tarih ve 26716 sayılı Resmi Gazete'de yayınlanan "İnternet Ortamında Yapılan Yayınların Düzenlenmesine Dair Usul Ve Esaslar Hakkında Yönetmelik" gereğince yer sağlayıcılar, "Yer sağlayıcı trafik bilgisini altı ay saklamakla, bu bilgilerin doğruluğunu, bütünlüğünü oluşan verilerin dosya bütünlük değerlerini zaman damgası ile birlikte saklamak ve gizliliğini temin etmekle" yükümlüdürler. Bu kapsamda, mesela bir web sayfası bulunduran sunucunun trafik bilgisi loglarının kanunen zaman damgası ile damgalanması zorunludur.
Log Bilgileri Nasıl Zaman damgası ile damgalanır?
Aşağıdaki çizim, bir log dosyasının üretildiği tarihten sonra değistirilmediğini gösteren zaman damgası ile damgalama yöntemlerinden birisidir. Bu yöntemle, ileriki bir tarihte oluşturulan zaman dosyasının değiştirilmediğini göstermek için benzer işlemin tekrarı yapılır, sonuç özet (hash) değerleri aynı bulunursa, dosyanın orjinal, zaman damgalandığı tarihten itibaren değişmediği sonucu çıkar.



Link: https://faq.cc.metu.edu.tr/faq/what-time-stamp-why-it-have-be-used-turkish

---

## Entry 2770

Question: Can I get an e-signature from another institution? I have an e-signature, can I use it?
Answer: 

 - It is possible to purchase electronic signature individually. Institutions authorized to obtain electronic signatures can be found at https://www.btk.gov.tr/elektronik-sertifika-hizmet-saglayicilari.
 - Public institutions are obliged to obtain their electronic certificates from the Kamu Sertifikasyon Merkezi (KamuSM) affiliated to TÜBİTAK UEKAE in accordance with the Prime Ministry circular.
 - If you already have an electronic signature kit, you can use it.
 - Individuals have to pay the Certified Electronic Signature (e-signature) fees obtained from alternative institutions.
 - If there is a problem in using e-signature certificates obtained individually from authorities other than KamuSM, in EBYS, a notification can be made to ebys-destek@metu.edu.tr via e-mail.


Link: https://faq.cc.metu.edu.tr/faq/can-i-get-e-signature-another-institution-i-have-e-signature-can-i-use-it

---

## Entry 2771

Question: Can I use my certificate in international correspondence?
Answer: 

There are a number of verifications for transactions made with electronic signatures. Just one of these; verification of the authority issuing the certificate and ensuring the accuracy of the certificate (root certificate) of this authority.
In this regard, the "Regulation on Procedures and Principles Regarding the Implementation of Electronic Signature Law" contains the following information about Foreign Electronic Service Providers (ECSP):
- Conditions regarding the legal consequences and acceptance of foreign electronic certificates are determined by international agreements.
- For end-user certificates to be used in different countries, the two countries need to sign an agreement by making a joint decision, and then, technical studies should be carried out with some methods to ensure that the root certificates of the countries trust each other. 
- Both countries must be working within the framework of international standards (such as ETSI TS 101 733, ETSI TS 101 903, CWA 14710 etc.).
For this reason, it is not possible to use the certificates obtained in EU member countries and other countries immediately. For this job, the two countries need to come together and make an agreement by making the necessary investigations and studies.


Link: https://faq.cc.metu.edu.tr/faq/can-i-use-my-certificate-international-correspondence

---

## Entry 2772

Question: How can I apply for renewal if my e-signature certificate has expired / is about to expire?
Answer: 

1. To renew your electronic signature that has expired or will expire, you must make a RENEWAL application by logging into https://e-imza.metu.edu.tr
*** IMPORTANT: Use the VPN service to access relevant addresses from outside the campus.
 You can visit https://faq.cc.metu.edu.tr/groups/vpn-service to get information about VPN service and its installation.
2. After your application is approved by TÜBİTAK KamuSM, a renewal application an e-mail sent to user's METU e-mail address from KamuSM.
3. After receiving the e-mail from KamuSM, the "Completing the e-Signature Applications of the Persons with Pre-Application" processes specified in the link must be completed.


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-apply-renewal-if-my-e-signature-certificate-has-expired-about-expire

---

## Entry 2773

Question: How can I find out the e-signature validity period?
Answer: 

Electronic signature certificates are valid for 3 years for Turkish citizens and 1 year for foreign nationals.
You can learn the validity period of your electronic signature in 5 different ways.
Two of the most practical are described below:
1. Connect to the http://eimza.metu.edu.tr page with your user code / password pair. The validity dates of all the certificates produced so far are shown on the relevant page.

Not: VPN service should be used to access this page outside of the campus. (for more information http://faq.cc.metu.edu.tr/groups/vpn-service)
2. In the EBYS application, when the PIN entry window is opened on the electronic signature or e-signature screens, "Valid" or "Expired" information is displayed in the "Validity period:" section under your user information.



Link: https://faq.cc.metu.edu.tr/faq/how-can-i-find-out-e-signature-validity-period

---

## Entry 2774

Question: How can I generate the PIN (password) code of my e-signature SIM card? How can I unlock the PIN?
Answer: 

If you have received a new CES (Certified Electronic Signature) card and you want to create a PIN, if you do not know the PIN code of your current CES, or if you have entered and locked your PIN by entering it incorrectly 3 times, you  need to perform the Unlocking process.
Link to KamuSM Lock Solving Help page:
https://kamusm.bilgem.tubitak.gov.tr/dokumanlar/yonergeler/nes/nes_kilit...
The steps to be followed are as follows:
1. At http://kamusm.gov.tr, click on the "ONLINE İŞLEMLER" tab marked in red in the upper right corner.
2. Click on "E-devlet ile Giriş" and then "E-devlet Kapısına Git" links. (Here it is possible to login with e-government password, mobile signature, e-signature or mobile banking)
3. On the page that opens, select "NES İşlemleri".
4. Proceed with the "PIN Oluşturma/Kilit Çözme" option.
5. For the next step, you need to have Java and Akis installed on your computer. (Relevant explanations and installation links are available on the page that opens)
 6. By following the steps on the page, run the KamuSMeImzaUygulamasi.jar file and copy the confirmation code (onay kodu) on the same page, and copy it to the relevant place in the opened KamuSMeImzaUygulamasi.jar application.

IMPORTANT NOTICE FOR MAC USERS
In MAC operating systems, when the KamuSMEimzaUygulamasi.jar application is downloaded and opened, the application is prevented from running within the framework of the security measures of the operating system. (You may encounter the following two warning screens)


In order to run the application, the following steps must be followed.
- Click the Apple icon in the upper left corner and select System Preferences here.
- On the page that opens, the General tab should be open.

As seen in the image above, opening KamuSMeImzaUygulamasi.jar file should be allowed in “Allow apps downloaded from” option.
7. After selecting your certificate on the page opened in the application, you can create a PIN for the new NES or create a new code for the locked PIN.



Link: https://faq.cc.metu.edu.tr/faq/how-can-i-generate-pin-password-code-my-e-signature-sim-card-how-can-i-unlock-pin

---

## Entry 2775

Question: How can I use E-signature in EBYS (Electronic Document Management System) [DSClient Application]? 
Answer: 

In order to use e-signature in EBYS (Electronic Document Management System), Java, e-signature reader drivers and DSClient application must be installed on the computer. 
For installation, you can follow the steps below (in Turkish):
for Windows;
1. How to install Java2. How to install e-signature drivers3. How to install DSClient application
for MacOS;
1. How to install Java2. How to install e-signature drivers3. How to install DSClient application
for Linux;
How can I use my e-signature in EBYS?
You can log in to EBYS with e-signature using the "Elektronik İmza ile Giriş" link at https://ebys.metu.edu.tr. First, plug the USB reader in which your e-signature SIM card is inserted to your computer. 

When you press the "Elektronik İmza ile Giriş" link, the card reader, certificate information (owner, identity number, serial number, etc.) will be displayed. After entering your PIN number, you can log in to EBYS application with the GREEN button.
 
Warnings That May Occur in the DSClient Application (in Turkish)
If you have problems using e-signature even though you have set up e-signature, or if you have different questions about e-signature, please check the frequently asked questions at https://faq.cc.metu.edu.tr/groups/e-signature.
The questions about EBYS can be asked to ebys-destek@metu.edu.tr.


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-use-e-signature-electronic-document-management-system-new-client

---

## Entry 2776

Question: How can I use my CES (e-signature) in TÜBİTAK Applications?
Answer: 

Akis card driver and Java must be installed for TÜBİTAK project applications.
 The use of e-signature for TÜBİTAK project applications is described in the document linked below: (Turkish)
 https://www.tubitak.gov.tr/sites/default/files/281/ardeb_e-imza_yardim_d...


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-use-my-ces-e-signature-tubitak-applications

---

## Entry 2777

Question: How is the KamuSM Certified Electronic Signature (E-signature) Application Process?
Answer: 

KAMUSM Certified Electronic Signature (CES) Application Process
The user has to login http://eimza.metu.edu.tr page with METU usercode and password. The appropriate choice should be chosen (First Application/Renewal/ID update) and the application must be submitted.
*** IMPORTANT: Use the VPN service to access relevant addresses from outside the campus.
 (You can visit https://faq.cc.metu.edu.tr/groups/vpn-service to get information about VPN service and its installation.)
The list of personnel requesting CES is sent to TÜBİTAK KamuSM by METU E-Signature Officer
An e-mail is sent to user's METU e-mail address by KamuSM.
After receiving the e-mail from TÜBİTAK KamuSM, the "Completing the e-Signature Applications with Pre-Application" processes specified in the link must be completed.
CES will be produced and delivered to the user by means of special courier.
 

Link: https://faq.cc.metu.edu.tr/faq/how-kamusm-certified-electronic-signature-e-signature-application-process

---

## Entry 2778

Question: How to e-sign a PDF document with Acrobat Reader DC?
Answer: 

With Acrobat Reader DC software, it is possible to sign an e-signature to a pdf document that was created before. There are two notices that need attention here:
1. KamuSM is not accepted as a secure root certificate provider in many operating systems. Therefore, root certificates produced by TUBITAK KamuSM must be downloaded and installed.
2. You must have installed the "Akis" driver suitable for your operating system. You can download it from the drivers page of KamuSM.
After running the Acrobat Reade DC software, follow the steps below:

Select "Edit" in the top menu and then "Preferences ..."





Select "Security (Enhanced)" on the left side and uncheck "Enbale Protected Mpode at Startup" under "Sandbox Protections" in the middle screen. Close the page by saying "OK".
You will need to restart Acrobat Reader DC.





When Acrobat Reader DC restarts, select 'Edit' in the Top menu and then 'Preferences ...' as in step 1.
Select "Signiture" on the left side and click the "More" button under "Identities & Trusted Certificates" in the middle screen.





Select "Digital IDs" on the left, under it, click "PKCS # 11 Modules and tokens" and click the "Attach Module" button




Akis module is "C: /Windows/System32/akisp11.dll" file. 




Select "Digital IDs" on the left, under "PKCS # 11 Modules and tokens", under "AKIS PKCS # 11 Library", go to "Akis".
Start the process of uploading your certificate by pressing the button with the "+" sign.





In the window that opens, type the "PIN" number required to access your certificate.
Then exit by saying "Cancel" in the window that opens.





You can see your certificate in "Akis" under "AKIS PKCS # 11 Library" under "PKCS # 11 Modules and tokens" under "Digital IDs" on the left.
Click the "Pencil" mark and select "Use for Signing".
Close all pop-up windows and return to the main Acrobat Reader DC screen.





Click the "Open" button in "Certificates" under "Tools" in Acrobat Reader DC tabs. If there is no "Certificates" it can be found under "Show more".





After the "Certificates" toolbar is created, click the "Digital Sign" button.





A warning will appear on the document for you to determine the place where you will sign your signature.





When you locate your signature, you will see the screen Acrobat Reader DC asks which certificate to use (Your e-signature must be attached) Select your certificate and press the "Contiune" button.





Enter your e-signature PIN in the "Enter the Digital ID PIN or Password…" field and press the "Sign" button.





A window will open for you to save the e-signed file. Save it wherever you see appropriate.


 

 

Link: https://faq.cc.metu.edu.tr/faq/how-e-sign-pdf-document-acrobat-reader-dc

---

## Entry 2779

Question: How to give E-APPROVAL for Certified Electronic Signature (e-signature)?
Answer: 

In KamuSM Certified Electronic Signature transactions, if you give one-time e-approval by using your e-signature, you can obtain Certified Electronic Signature (CES) quickly without the need to send documents for your future requests. To do this, you need to follow the steps below:
In order to carry out the relevant operations in KamuSM, Java and Akis installations must be done.
1. Go to http://kamusm.gov.tr.
2. Click on the "ONLINE İŞLEMLER" tab.
3. After selecting "E-Devlet ile Giriş", click on the "E-devlet Kapısına Git" link. Sign in with your ID number, CES (NES) or mobile banking.
4. Select "NES İŞLEMLERİ".
5. Select "E-ONAY İŞLEMLERİ":

6. The steps to be followed are described in detail on the page that opens. Give your E-APPROVAL by following the steps.
PS: If you have e-approved before, the system will show you the option your e-approve; you can just exit without any transactions.


Link: https://faq.cc.metu.edu.tr/faq/how-give-e-approval-certified-electronic-signature-e-signature

---

## Entry 2780

Question: I cannot access it with the NES application access password come from Kamu SM, what should I do?
Answer: 

Certified Electronic Signature (CES/NES) application access password validity period is 6 months.
After 6 months, the application must be renewed by the Institution E-signature Officer.
To do this, go to http://eimza.metu.edu.tr and log in with your METU user code&password and submit your application to the METU Institution E-signature Officer.


Link: https://faq.cc.metu.edu.tr/faq/i-cannot-access-it-nes-application-access-password-come-kamu-sm-what-should-i-do

---

## Entry 2781

Question: I deleted the Certified Electronic  Signature (E-signature) Application E-mail from Kamu SM. What should I do?
Answer: 

If the Certified Electronic Signature application e-mail sent from Kamu SM is accidentally deleted, an automatic password e-mail is sent by the system once a week to the e-mail address notified to Kamu SM from our institution. Instead of waiting for this period,  it's possible to send the email again by following the steps below.
1. On the www.kamusm.gov.tr web site, click “NES Başvuru Erişim Parolası Gönder” from the “BAŞVURU” section on the main page.

2. On the new page that opens, a new application access password can be sent by entering the user's ID and METU e-mail address. 
 
 


Link: https://faq.cc.metu.edu.tr/faq/i-deleted-certified-electronic-signature-e-signature-application-e-mail-kamu-sm-what-should-i-do

---

## Entry 2782

Question: I don't have an e-signature, how can I get it?
Answer: 

It is possible to obtain an electronic signature with individual or institutional payment. Public institutions are obliged to obtain their electronic certificates from the Kamu Sertifikasyon Merkezi (KamuSM) affiliated to TÜBİTAK UEKAE in accordance with the Prime Ministry circular. Personnel who can obtain an electronic signature with institutional payment can make an E-signature request by filling out the form at
http://e-imza.metu.edu.tr/
with METU username and password.
Please use the VPN service to access the relevant address from outside the campus. You can visit https://faq.cc.metu.edu.tr/tr/groups/vpn-service for information about the VPN service and its installation.
For those who want to purchase an electronic signature individually, institutions authorized to provide electronic signatures can be learned from https://www.btk.gov.tr/elektronik-sertifika-hizmet-saglayicilari. Indiv... have to pay the Certified Electronic Signature (e-signature) fees obtained from alternative institutions.
If you have a previously purchased electronic signature card reader, you can use it.


Link: https://faq.cc.metu.edu.tr/faq/i-dont-have-e-signature-how-can-i-get-it

---

## Entry 2783

Question: I lost my e-signature / it was stolen, my credentials have been updated; what should I do?
Answer: 

In case of "Lost/Stolen" or "Credential Update", the user has to pay for the certificate him/herself.
The user can make the transactions for the lost or stolen e-signature certificate him/herself on the http://kamusm.gov.tr ​​page.
(KamuSM does not have Englih Pages; please follow the instructions below)
 - Go to http://kamusm.gov.tr. Click on the Online İşlemler button in the upper right corner.
 - Login with E-Devlet
 - Click on NES İşlemleri
 - Select Bireysel İşlemler
 - Select Başvuru İşlemleri
 - Select Kişi Ödemeli Başvurular
 - Select TC Yükseköğrenim Kurumu
 - Fill in the form by providing the relevant personal information on the upcomig page. (YES must be selected for "Sertifikam Internetten Yayınlansın mı?"); approve and finish the procedure.
 
 


Link: https://faq.cc.metu.edu.tr/faq/i-lost-my-e-signature-it-was-stolen-my-credentials-have-been-updated-what-should-i-do

---

## Entry 2784

Question: I retired, I no longer work at METU, can I get an e-signature?
Answer: 

Since METU is a state institution, memberos of METU can only obtain e-signature through TÜBİTAK KamuSM.
For e-signature requests made from TÜBİTAK KamuSM through our institution, it is required that the person be a full-time or part-time METU staff member.
Personal applications can be made from one of the Electronic Certificate Service providers listed below;
E-Trust (https://www.e-guven.com)
TürkTrust (http://www.turktrust.com.tr)
E-Tugra (http://www.e-tugra.com.tr)
e-SignatureTR (http://www.e-imzatr.com)


Link: https://faq.cc.metu.edu.tr/faq/i-retired-i-no-longer-work-metu-can-i-get-e-signature

---

## Entry 2785

Question: I've lost my e-signature card reader. What should I do?
Answer: 

If you have lost your existing card reader, you can individually request a new card reader via KamuSM at the address below.
https://ebasvuru.kamusm.gov.tr/kartokuyucu
Card reader fee will be paid individually and cannot be covered by the institution.


Link: https://faq.cc.metu.edu.tr/faq/ive-lost-my-e-signature-card-reader-what-should-i-do

---

## Entry 2786

Question: What is E-Signature?
Answer: 

E-signature or Qualified Electronic Certificate (QEC) is the electronic text equivalent of the wet-signature used in all electronic environments.  In addition, it can be used as an authentication tool in various online or offline environments.
According to Electronic Signature Law No. 5070 dated January 15, 2004, the secure electronic signature given by the authorized Electronic Certificate Service Providers has the same legal consequences as the signed signature.
E-signature created in accordance with the law provides a legal basis for computer or electronic letter approval processes and removes the paper.
The person who would like to make a declaration of intention can use e-signature in the institution’s document flow system, web services, or e-government services.


Link: https://faq.cc.metu.edu.tr/faq/what-e-signature

---

## Entry 2787

Question: What should be done in case of a change of surname? Can I still use my e-signature?
Answer: 

In case of surname change, you cannot use your e-signature kit. You need to renew your e-signature kit with a request for information updates.
You can get relevant information from the link http://faq.cc.metu.edu.tr/faq/i-lost-my-e-signature-it-was-stolen-my-credentials-have-been-updated-what-should-i-do


Link: https://faq.cc.metu.edu.tr/faq/what-should-be-done-case-change-surname-can-i-still-use-my-e-signature

---

## Entry 2788

Question: Where should the wet signed e-signature application form be submitted?
Answer: 

In e-signature applications, form must be filled by following by the e-mail containing the "application password" sent from KamuSM, and signed with a wet signature and sent to KamuSM via regular mail at the address below.
Address:
Kamu Sertifikasyon Merkezi
TÜBİTAK Gebze Yerleşkesi (İdari Bina)
P.K. 74, Gebze 41470 KOCAELİ
Detailed information on the application process can be found at http://faq.cc.metu.edu.tr/faq/how-kamu-sm-certificate-electronic-signature-e-signature-application-process


Link: https://faq.cc.metu.edu.tr/faq/where-should-wet-signed-e-signature-application-form-be-submitted

---

## Entry 2789

Question: Where will I use the e-signature? Is it compulsory?
Answer: 

It should be used in internal processes such as Electronic Document Management System (EBYS), Financial Management System v2 or inter-institutional processes such as TÜBİTAK applications.
It is predicted that the use of electronic certificates will become widespread in the future.
It is not mandatory to obtain an e-signature certificate if you will not use it for the above-mentioned purposes.


Link: https://faq.cc.metu.edu.tr/faq/where-will-i-use-e-signature-it-compulsory

---

## Entry 2790

Question: Can Linux based operating systems be affected by viruses?
Answer: 

Although Linux based operating systems be affected by viruses, there is no immense virus activity. In general updating against viruses, which would try to seep in through the shell or the gaps in the software being used, is accepted as the sufficient precaution.


Link: https://faq.cc.metu.edu.tr/faq/can-linux-based-operating-systems-be-affected-viruses

---

## Entry 2791

Question: How do I find out that my PC is infected by a virus?
Answer: 

Antivirus software programs, once installed, are the the most effective detection and deletion means, as long as they are actively and regularly updated. (Symantec Norton, McAfee etc.) 
Following the link below, you can freely download Symantec virus scan software from software.metu.edu.tr and scan your computer. Delete the viruses detected.


Link: https://faq.cc.metu.edu.tr/faq/how-do-i-find-out-my-pc-infected-virus

---

## Entry 2792

Question: Is there a licensed antivirus software at METU? If so, where can I download/get it from?
Answer: 

In METU Symantec Antivirus software is licensed and being used through out the campus. 
It is available for download at https://software.cc.metu.edu.tr  or you can also get them from your department computer coordinator. 
https://software.cc.metu.edu.tr address is accessible to all METU members. Login this address using your user code and password. Students who reside at the dormitories can also get this software from the security CD supplied to the Dormitory Management.
You can access Frequently Asked Questions on Symantec via http://faq.cc.metu.edu.tr/symantec
 


Link: https://faq.cc.metu.edu.tr/faq/there-licensed-antivirus-software-metu-if-so-where-can-i-downloadget-it

---

## Entry 2793

Question: What is Spyware?
Answer: 

Spyware is the name given to software that collects computer users' personal information without the users' willing or knowledge. Other terminology such as "malware" and "adware" which have a general and different meaning may also be used instead of spyware.
Spyware can perform various actions, such as keeping track of the keyboard when typing, keeping a record of the visited web sites, scanning the data on the hard disk, tracking the searches performed on the internet etc. which all mean a breach of secrecy of personal information. As a result, it can get hold of the passwords of e-mail, bank account etc. illegally, display pop-up windows and/or send spam e-mails for "personal advertisements" which are annoying, use up network and computer resources which causes the computer slow down, lag in opening up web pages, longer boot and action durations in general.
Spyware software are different from viruses, since they are not openly illegal and not designed for purposes that would directly pose a threat to the user, and install themselves onto the computer with the user_x0092_s consent or activities. Furthermore spyware do not copy themselves from one computer to another, like viruses do. However, the consent is obtained without any clarifying explanation on how these malicious software will work and perform on the computer.
Usually the user receives a notice asking to install an annex (add-on, extension, plug-in) on the web browser in order to open up or display the web page properly, and upon giving the authorization the spyware is installed. Also a web site that provides a free service (software, music, video, online games etc.) may impose the software to be installed on the computer. Similarly, some free software install spyware secretly or by trying to get the consent of the user while installing their software. Such sites or software developers sell and thus obtain a gain for having the software installed by selling the users_x0092_ personal or statistical information to people or groups who aim to advertise etc.


Link: https://faq.cc.metu.edu.tr/faq/what-spyware

---

## Entry 2794

Question: What should I do after removing the virus from my computer?
Answer: 

If your IP (Internet Protocol) access has been restricted by METU-CC you ask to hotline@metu.edu.tr to find out the reason.
After you remove the virus, you should inform METU-CC by sending an e-mail to cc-sec@metu.edu.tr to restore your network connection.
You should check and install the latest system updates from "Windows Update" module in Windows Settings.


Link: https://faq.cc.metu.edu.tr/faq/what-should-i-do-after-removing-virus-my-computer

---

## Entry 2795

Question: What should I do to protect my computer against spyware?
Answer: 

The most effective way of avoiding such software is to refrain from certain user habits that cause these to spread. Authorizing all the inquiry or notice windows while surfing the internet leads to the installation of many unnecessary software. People who have higher expertise and experience stay away from problems without making use of anti-spyware software. Therefore it is imperative that a dialogue or a notice screen encountered on any web page not be authorized without really understanding what is wanted or without consulting someone who might have an insight.
In addition, some free software such as internet accelerator, rapid download, file sharing etc. install spyware along with their functionality. Even more, there are spyware installed on computers that claim that they themselves are anti- spyware and that they will clean up the malicious software in the computer thus deceiving the unknowing user. Before installing any such free software, you should search on the internet about them or consult for technical support from experts.
Anti-spyware
Anti-spyware are security software developed to protect computers from spyware. Some anti-virus software are capable of protecting the computer against well-known spyware, however, anti-spyware have specialized on removing, deleting or making obsolete the spyware and updating themselves for newly developed spyware. Although some are paid, there are also free, competent and widely used ones.
Windows Defender
It is the anti-spyware developed to protect Windows operating systems from spyware and provided free to the licensed Windows users. This software is already installed on Windows Vista or newer operating systems. This product automatically updates itself, recognizes spyware and blocks them from appending themselves to the system, furthermore scans and eradicates those that have already been added. You have to activate it from Windows Security settings, by clicking "Actions Recommended"  

 

Link: https://faq.cc.metu.edu.tr/faq/what-should-i-do-protect-my-computer-against-spyware

---

## Entry 2796

Question: What should I do to protect my computer against viruses?
Answer: 

Install a licensed antivirus program such as Symantec, Norton, McAfee etc. and always keep it updated. An antivirus program that has not been updated is helpless against newly devised viruses.
Keep your operating system updated. You can update your Windows operating system from Settings -> Windows Update.
Instead of Microsoft Outlook or Outlook Express, prefer to use Mozilla Thunderbird or any of the webmail services provided by METU-Mail since these are more reliable against viruses that seep through gaps in Microsoft Outlook ve Outlook Express.
Unless necessary do not turn on file sharing. If it is a must, set password requirement on and select read-only file sharing.
Unless needed, do not set up server type operating systems such as Microsoft Windows Server etc.
Do not operate IIS (Internet Information Services) as a web server that have not been updated.
Set your computer to be booted only from the hard disk. Always back up your crucial files/information. Do not run macros on the office programs that you do not know.
For not to be affected of viruses which infect through Microsoft Office, use alternative Office programs such as OpenOffice.org.
Do not run the executable files which have been sent by e-mail as attachment unless you verify it from the sender.
Use anti-spyware to protect your computer against spyware which aims to collect your personal information.
 


Link: https://faq.cc.metu.edu.tr/faq/what-should-i-do-protect-my-computer-against-viruses

---

## Entry 2797

Question: What should I do, in case of virus detection/infection?
Answer: 

In order to delete a virus from the computer scan all your hard disks with updated antivirus software and after deleting the virus, perform system updates so as not to encounter another virus problem.
In order to do that, install Symantec antivirus software which can be downloaded free from software.cc.metu.edu.tr address. Remove the network connection cable an reboot your computer in safe mode and start a virus scan with the updated antivirus software. Delete all the viruses detected/found during scanning.
If the operating sytem updates are not installed, after the deletion is completed, the virus can affect the computer again. That is why you should do the operating system and antivirus software updates frequently.


Link: https://faq.cc.metu.edu.tr/faq/what-should-i-do-case-virus-detectioninfection

---

## Entry 2798

Question: Some of e-mails, although not spam, arrive at the SPAMBOX folder. What should I do?
Answer: 

Forward the e-mail with full header information and the body part by opening a support ticket via https://itsupport.metu.edu.tr. You can get information about how to view the full header of a message from this link.
If you are using Horde, mark the e-mails that are not spam in your SPAMBOX folder and click Report as Innocent in order to report them as clean to spam filter.


Link: https://faq.cc.metu.edu.tr/faq/some-e-mails-although-not-spam-arrive-spambox-folder-what-should-i-do

---

## Entry 2799

Question: What is Spam and Malware?
Answer: 

Spam is an unsolicited random e-mail that has been sent without the consent of the recipient.
Malware is the abbreviation for "malicious software". It is the general name given to unwanted and nasty scripts/codes like viruses, trojans etc. Such codes can enter your PC through an attachment of a program, or they can be downloaded unknowingly at the background from a web site you are browsing. Even the updated antivirus software may not always succeed in detecting malware.
Such e-mail messages or software are sent to collect e-mail addresses, passwords or personal information of users to be used for commercial purposes. They can sometimes be sent to capture the information on your PC or to follow up the sites you have visited on the Internet.


Link: https://faq.cc.metu.edu.tr/faq/what-spam-and-malware

---

## Entry 2800

Question: What is SPAMBOX?
Answer: 

The received e-mail messages are filtered by a spam filter which is running on central mail server. The messages that are marked as spam are directed to a folder located under your mail directory, and it is named as SPAMBOX. You can access the SPAMBOX through Horde, SquirrelMail or pine programs; or e-mail clients using IMAP services.
Sometimes a normal e-mail can be marked as spam by the filter. Therefore you should check your SPAMBOX periodically.
The messages on the SPAMBOXes that extend the limits will be moved to another folder automatically in the same directory under the name of SPAMBOX.date and a notification e-mail will be sent. These moved SPAMBOXes will be deleted within a specified period automatically.


Link: https://faq.cc.metu.edu.tr/faq/what-spambox

---

## Entry 2801

Question: What measures does the CC take regarding spam/bogus e-mail?
Answer: 

The messages that arrive at the CC mail server are categorized into spam which are directed to the SPAMBOX folder of the users, some are identified as containing a virus and automatically discarded, the actual messages that do not contain a virus or are not classified as spam are placed at the INBOX folders of the users.
Spam messages are filtered by the CC, by means of the spam filter operating on the e-mail server. E-mail identified as spam by this filter is directed to a specific e-mail box, referred to as SPAMBOX, located within the main mail folder of the recipient.
The main reason for sending spam messages to the SPAMBOX rather than deleting them is to give our users a chance to check if the identification was correct and not to lose a message that has mistakenly been identified as spam and sent to the SPAMBOX.
The spam filter software is dynamic and is able to increase its success rate by learning from our users when identifying a message as spam or an actual e-mail message. In the learning process, thanks to the frequency of number of words used, sender address, and other such header information, used in e-mail messages defined as clean or spam, the spam filter software decides on the probability of an incoming e-mail to be spam and marks those with a certain threshold level as spam. Then, these e-mail messages are carried on to SPAMBOXes. Theoretically, it is possible for this filter to identify messages correctly with 99.9 % accuracy. When the filter is constantly fed with clean/spam messages, its success rate increases.
The expert staff at the CC, after much research done, have decided this filter system to be the best solution for METU users, and after meticulous teaching work on defining clean/spam messages to the filter, they have put the system into application. The software is at a process of constant learning due to its technical structure and renews itself according to the customer profile.


Link: https://faq.cc.metu.edu.tr/faq/what-measures-does-cc-take-regarding-spambogus-e-mail

---

## Entry 2802

Question: What should I do with spam e-mail?
Answer: 

Forward the e-mail with full header information and the body part by opening a support ticket via https://itsupport.metu.edu.tr in order to have the e-mail be defined as spam to the spam filter. You can get information about how to view the full header of a message from this link.
If you are using Horde, mark the spam e-mails and click Report as Spam in order to define them as spam to spam filter.
With the help of the feedback from users, spam filter will be able to differentiate spam messages more effectively.


Link: https://faq.cc.metu.edu.tr/faq/what-should-i-do-spam-e-mail

---

## Entry 2803

Question: How can I apply for a new e-list?
Answer: 

To create a new list on the list server of METU, the academic/administrative department or the adviser/administrator of the student group must apply to METU Computer Center by filling out the "Application Form". A user code and a password defined on the central servers of the university are required to access the application form. The list owner will be notified, if the request to open a new list is deemed appropriate by the Center.
A user must fill out the "Application Form" to be able to open the list she/he wants. The information required on this form covers explanation about the list, the aim of the list, the owner of the list and the type of the list. Only the academic and administrative personnel can access the form using their usernames and passwords defined on the central servers. The procedure for opening a list on METU Electronic List Server is handled by CC Informatics Group.
The name of the list is required to be relevant to the aim and the subject of the list. In addition generic names and names which can possibly be used as user names should not be entered as list names. In case of such list name requests CC Informatics Group suggests appending an "-l" at the end of the list name or adding another suitable suffix or prefix. eg: If the user requests the list name "cinema", it is suggested that the name may be changed as odtu-cinema or cinema-l.
Moreover, communication lists are requested for some courses during the academic term. In the applications made for these courses, list name is required to be a combination of the related department's ECS user code and the course code. If a list is requested for a course which is given in more than one section, the list name is defined by adding the section number to the name of the list for the course: Eg: econ123id234-2
For the requests from METU Northern Cyprus Campus, list name must start with "ncc-" in addition to the criteria above.
Departments may own electronic lists for the purpose of communicating with their students, in case list administration is handled by their own personnel. Names of such lists that can be defined for different classes are as below: 1. class -> dept-freshman 2. class -> dept-sophomore 3. class -> dept-junior 4. class -> dept-senior Master and Doctorate Students -> dept-graduate or dept-gAll Undergraduate Students -> dept-undergraduate or dept-ug
Similarly, if requested by departments, general lists with the names, dept-students, dept-staff and dept-faculty can be defined for respectively the department students, staff or faculty members."dept" is replaced with the ECS user code of the department.


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-apply-new-e-list

---

## Entry 2804

Question: How a list can be set  for everyone (member-or-not) to be able to send message to the list?
Answer: 

For ALL (member or not) to be able to send a message to the list (send-by-all):
(a) The setting at Membership Management > Membership List > Additional Member Tasks > Set everyone's moderation bit, including those members not currently visible is selected as OFF.(b) The setting at Privacy options > Sender filters > Member filters > By default, should new list member postings be moderated? is selected as NO.(c) The setting at Privacy options > Sender filters > Non-member filters > Action to take for postings from non-members for which no explicit action is defined. is selected as ACCEPT.


Link: https://faq.cc.metu.edu.tr/faq/how-list-can-be-set-everyone-member-or-not-be-able-send-message-list

---

## Entry 2805

Question: How a list can be set  for only the list administrator to be able to send message to the list?
Answer: 

For only the list administrator to be able to send messages to the list (send-by-owners):
(a) The option for Membership Management > Membership List > Additional Member Tasks > Set everyone's moderation bit, including those members not currently visible is set to ON.(b) The option for Privacy options > Sender filters > Member filters > By default, should new list member postings be moderated? is set to YES.
IMPORTANT NOTE: For the messages with viruses or spam messages that appear to be coming from the moderator(s), as a measure you can make the below settings effective.
i. The e-mail addresses authorized to send messages to the list SHOULD NOT BE a member of the list. If the authorized address(es) belong to the moderator(s) the same is effective for them as well. If these address(es) is(are) member(s) of the list, their membership(s) is(are) cancelled.ii. The e-mail address(es) to be authorized to send messages to the list should be entered at Privacy options >Sender filters > Non-member filters > List of non-member addresses whose postings will be immediately held for moderation as one e-mail address per line.iii. The setting for Privacy options > Sender filters > Member filters > Action to take when a moderated member posts to the list. is selected as either "Reject" or "Discard".vi. After these settings the e-mail address(es) authorized to send messages to the list can send to the list. The messages sent from these address(es) are submitted in electronic media to the attention of the list administrator and/or the moderator to be approved.v. The list administrator with the administrator password, if assigned, moderator(s) with the moderator password, access the http://mailman.metu.edu.tr/mailman/admindb/LIST-NAME page approve the message(s) waiting for attention. Only then the message(s) is(are) distributed to the list.


Link: https://faq.cc.metu.edu.tr/faq/how-list-can-be-set-only-list-administrator-be-able-send-message-list

---

## Entry 2806

Question: How a list can be set  for only the moderator to be able to send message to the list?
Answer: 

 For only the moderator to be able to send messages to the list (moderated-edit list):
(After these settings are done, the list becomes a one way list, in other words it becomes an announcement list.)
(a) Entry is done on the General Options > The list moderator email addresses field as one line per one moderator address.(b) The option ON is selected for Membership Management > Membership List > Additional Member Tasks > Set everyone's moderation bit, including those members not currently visible.(c) The option YES is selected for Privacy options > Sender filters > Member filters > By default, should new list member postings be moderated?.
IMPORTANT NOTE: For the messages with viruses or spam messages that appear to be coming from the moderator(s), as a measure you can make the below settings effective.
i. The e-mail addresses authorized to send messages to the list SHOULD NOT BE a member of the list. If the authorized address(es) belong to the moderator(s) the same is effective for them as well. If these address(es) is(are) member(s) of the list, their membership(s) is(are) cancelled.ii. The e-mail address(es) to be authorized to send messages to the list should be entered at Privacy options >Sender filters > Non-member filters > List of non-member addresses whose postings will be immediately held for moderation as one e-mail address per line.iii. The setting for Privacy options > Sender filters > Member filters > Action to take when a moderated member posts to the list. is selected as either "Reject" or "Discard".vi. After these settings the e-mail address(es) authorized to send messages to the list can send to the list. The messages sent from these address(es) are submitted in electronic media to the attention of the list administrator and/or the moderator to be approved.v. The list administrator with the administrator password, if assigned, moderator(s) with the moderator password, access the http://mailman.metu.edu.tr/mailman/admindb/LIST-NAME page approve the message(s) waiting for attention. Only then the message(s) is(are) distributed to the list.


Link: https://faq.cc.metu.edu.tr/faq/how-list-can-be-set-only-moderator-be-able-send-message-list

---

## Entry 2807

Question: How a list can be set  to be displayed at the Mailman web main page?
Answer: 

For the list to be displayed at the Mailman web main page (visible-list):
(a) The setting at Privacy options > Subscription rules > Advertise this list when people ask what lists are on this machine? is selected as YES. (If the list is not to be seen, NO will be selected.)


Link: https://faq.cc.metu.edu.tr/faq/how-list-can-be-set-be-displayed-mailman-web-main-page

---

## Entry 2808

Question: How a list can be set for  only the list members to be able to send message to the list?
Answer: 

 For only the list members to be able to send a message to the list (send-by-subscribers):
(a) The setting at Membership Management > Membership List > Additional Member Tasks > Set everyone's moderation bit, including those members not currently visible is selected as OFF.(b) The setting at Privacy options > Sender filters > Member filters > By default, should new list member postings be moderated? is selected as NO.(c) The setting at Privacy options > Sender filters > Non-member filters > Action to take for postings from non-members for which no explicit action is defined. is selected as HOLD.


Link: https://faq.cc.metu.edu.tr/faq/how-list-can-be-set-only-list-members-be-able-send-message-list

---

## Entry 2809

Question: How can I define a common password for the electronic lists I have subscribed? (in Turkish)
Answer: 

E-liste servisindeki altyapı gereği, kullanıcıların üye oldukları her bir e-liste için farklı e-liste şifreleri tanımlanmaktadır. Dileyen kullanıcılarımız kolaylık olması açısından, tüm e-listeler için ortak bir e-liste şifresi tanımlayabilirler. Bunun için aşağıdaki işlemlerin yapılması gerekmektedir.
Not: Güvenlik önlemi olarak, merkezi kullanıcı kodları için kullanılan şifrelerin e-liste şifresi olarak kullanılmaması önerilmektedir.
Bir kullanıcı öncelikle üye olduğu herhangi bir listeye gönderilmiş bir mesajın sonunda yer alan e-liste web arayüzü bağlantısını kullanarak o e-listenin ayarları ile ilgili değişikliklerin yapılabildiği sayfaya (http://mailman.metu.edu.tr/mailman/listinfo/liste_adi) girmelidir.

Bu sayfanın en alt bölümünde yer alan e-posta adresi bölümüne, bu e-listeye üye olmak için kullandığı e-posta adresini yazarak, _x0093_Listeden çık veya seçeneklerimi düzenle_x0094_ isimli butona tıklamalıdır.

Eğer e-liste şifresi daha önceden girilmiş ise, aşağıdaki şekilde olduğu gibi e-liste üyelik ayarlarının değiştirilebildiği ekran görünecektir. Aksi durumda, e-liste şifresi kullanılarak giriş yapılmalıdır:

Üye olduğu tüm e-listelere yönelik ortak bir şifre tanımlamak isteyen kullanıcı bu sayfada yer alan _x0093_Şifre Değişimi_x0094_ bölümüne mevcut e-liste şifresini veya kullanmak istediği herhangi bir şifreyi yazıp, _x0093_Şifremi Değiştir_x0094_ butonuna _x0093_Global Olarak Değiştir_x0094_ seçeneği seçili olacak şekilde tıklamalıdır.

Bu işlem başarılı bir şekilde gerçekleştirildiği takdirde, ekranda _x0093_Şifre başarıyla değiştirildi._x0094_ şeklinde bir mesaj görüntülenir. Kullanıcı tarafından tanımlanan yeni şifre artık aynı e-posta adresi ile üye olunan mevcut tüm e-listelerde kullanılabilir.
Şifre değiştirme işlemi sırasında _x0093_Global Olarak Değiştir_x0094_ seçeneği seçili olmadığı durumda, sadece söz konusu e-listenin şifresi değiştirilmiş olur.
"Global Olarak Değiştir" seçeneği ile kullanıcının o ana kadar üye olduğu tüm listelerin şifreleri değiştirilir. Bu işlem sonrasında üye olunacak yeni e-listelerde de aynı şifrenin kullanılabilmesi için bu işlemin her üyelikten sonra tekrarlanması gerekir. Bu işlem yapılmadığında yeni üye olunan e-listelerde, üye olurken Mailman tarafından otomatik olarak tanımlanıp kullanıcıya gönderilen şifreler kullanılır.


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-define-common-password-electronic-lists-i-have-subscribed-turkish

---

## Entry 2810

Question: How can I reach to the general information about MAILMAN ?
Answer: 

During the first half of the year 2006, the software being used for providing Electronic List Services in METU has been aborted and all the electronic lists in use have gradually been transferred from the software ListProcessor, to Mailman software.
On this page and the pages linked from this page, detailed information about Mailman is given in order to provide support to the existing list members and administrators.
List Usage Interface:http://mailman.metu.edu.tr/mailman/listinfo
List Administration Interface:http://mailman.metu.edu.tr/mailman/admin
Help Document for the List Members:mailman-member.pdf [PDF File, Size: 83 KB]
Help Document for the List Administrators:mailman-admin.pdf [PDF File, Size: 92 KB]
To Get Information about Mailman:http://www.gnu.org/software/mailman/index.html
• Mailman Frequently Asked Questions (FAQ) Page:http://wiki.list.org/display/DOC/Frequently+Asked+Questions
Contact Address for Questions and Problems:mailmanmetu.edu.tr
 

Link: https://faq.cc.metu.edu.tr/faq/how-can-i-reach-general-information-about-mailman

---

## Entry 2811

Question: How can I unsubscribe from the  "abc-l" list? (in Turkish)
Answer: 

Liste üyeliğinden çıkış için http://mailman.metu.edu.tr/mailman/listinfo/abc-l adresinde sayfanın en alt kısmında yer alan "abc-l listesinden çıkmak, bir şifre hatırlatıcı istemek, veya üyelik seçeneklerinizi değiştirmek için üyelik e-posta adresinizi girin" yazılı bölüme listeye üyelik için kullandığınız e-posta adresinizi girip butona basınız.
Karşınıza gelen sayfada yer alan "Üyelikten Çık" butonuna basınız.
Belirttiğiniz e-posta adresi listeye üye bir adres ise üyelikten çıkış için bu adrese bir onay mesaji gönderilecektir (Bazen mesajların alındığı adres ile listeye üye olan adres farklı olabilmektedir. Birden fazla e-posta adresi kullanıyorsanız bu adresler arasında yönlendirme olabilir. Üyelikten çıkış işlemini listeye üyelik için kullandığınız adres üzerinden gerçeklestiriniz.)
E-posta adresine gelen onay mesajındaki linke tıklayarak erişeceğiniz web sayfasında üyelikten çıkış talebinizi bir kere daha onaylamalısınız.
Bazı listelerde üyelikten çıkış işlemlerinin liste yöneticisi tarafından onaylanması tercih edilmektedir. Eğer bu işlemleri gerçekleştirdiğiniz halde listeden mesaj almaya devam ediyorsanız abc-l-ownermetu.edu.tr adresinden liste yöneticisiyle iletişime geçiniz.
(Yukarıda geçen "abc-l" ifadesi liste ismi için örnek olarak verilmiştir.abc-l yerine çıkmak istediğiniz listenin adını yazmalısınız.)


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-unsubscribe-abc-l-list-turkish

---