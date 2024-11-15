## Entry 2812

Question: How can I use MAILMAN Interface as a List Administrator? 
Answer: 

This page provides information about how the people who are list administrators can make use of the electronic list services by using the Mailman software. Mailman software provides web interfaces produced in various languages, specifically in Turkish and in English, to be used with electronic list services. Assuming that the list users would primarily use the English web interface, section titles and information messages on this page are given in English.
To access the information or to work on the list of which you are the administrator:
(1) From the http://mailman.metu.edu.tr/mailman/admin address, click on the list you are administering.
(2) On the window that comes up on the screen at the http://mailman.metu.edu.tr/mailman/admin/LIST-NAME address, the administrator password has to be entered:Once the correct password is entered, a similar screen to the below comes up:
(3) The sections on the list administration interface:
(a) General Options is the interface to make changes on the features like, short or long list name, add/delete/change list administrator, assigning the list moderator, list descriptions, welcome or goodbye messages. It can be accessed from thehttp://mailman.metu.edu.tr/mailman/admin/LIST-NAME/general address.

To display the short name of the list in upper case or lower case characters:Change is made on the field, "The public name of this list (make case-changes only).":e.g. a short list name may be displayed as Test, TEST, Test etc.


To make changes on the list administrator/add a new one/delete an existing one:Changes are made on the field, "The list administrator email addresses. Multiple administrator addresses, each on separate line is okay." New administrators can be added as one e-mail address per line. Erasing an existing line would delete that administrator.


To assign a moderator to the list:Changes are made on the field, "The list moderator email addresses. Multiple moderator addresses, each on separate line is okay." New moderators can be added as one e-mail address per line. Erasing an existing line would delete that moderator. If the field is left empty, there would be no moderator assigned.


To define the long name of the list:To define the long name of the list that is going to appear at the address http://mailman.metu.edu.tr/mailman/listinfo, on the field "A terse phrase identifying this list." is entered the name. If this field is left empty, no long name would be seen and the comment [no description available] will be displayed.e.g. Electronic list service TEST list.


To show a description of the list:If a description is preferred regarding a list, when the http://mailman.metu.edu.tr/mailman/listinfo/LIST-NAMEaddressed page is accessed, the information is supplied in the field "An introductory description - a few paragraphs - about the list."e.g. TEST list is a closed list to experiment on, in order to trouble shoot probable problems of electronic list services and to improve the services, and is only accessible to the CC staff.


To remind the list members of their password monthly:To facilitate this option, in the field "Send monthly password reminders?", "Yes" option is selected; if no reminder is wanted, "No" option is selected.


To annex to the welcome message sent to the new members:A standard welcoming message is normally sent to the new members when they become a member of the list (if needed, this feature can be changed). To add messages specific to the list or information deemed necessary by the administrator to the standard welcome message, the field "List-specific text prepended to new-subscriber welcome message" can be filled in. (Note: In the script on the page http://mailman.metu.edu.tr/mailman/edithtml/LIST-NAME/subscribeack.txt necessary changes can be made on the standard welcome message.)


To send goodbye message to the members leaving:A standard goodbye message is normally sent to the members when they leave the list (if needed, this feature can also be changed). To add messages specific to the list or information deemed necessary by the administrator at the end of the standard goodbye message, the field "Text sent to people leaving the list." can be filled in.


To determine the membership settings of new members:There are various membership settings options for the new members added to the list. The list administrator can make changes in the settings according to his/her preference in the field, "Default options for new members joining this list."


To limit the size of the messages sent to the list:Normally, the size of the maximum message is 40 KB (including the attached file to the message). The list administrator can enlarge or shorten this size in accordance with the need. If the change is necessary, the value in the field, "Maximum length in kilobytes (KB) of a message body." can be changed. If zero (0) is entered in this field, there would be no limit to the size of the message.

(b) To assign new passwords for the list administrator or the moderator: If the need arises to change the password of the list administrator or, if there is one, the moderator, the change can be made on the screen that comes up from the interface on the page http://mailman.metu.edu.tr/mailman/admin/LIST-NAME/passwords.(c) Language options of the list: The choice of the language(s) to be used for a list is made on the interface that comes up from the address http://mailman.metu.edu.tr/mailman/admin/ LIST-NAME /language. Firstly, the languages to be used in the interface are indicated from the field, "Languages supported by this list." (Languages of Turkish and English must be selected for every list.). Afterwards, from the "Default language for this list." field, the default language is selected.
(d) To manage membership: To add or delete a member or to change the membership settings of the members of the list, the interface at the http://mailman.metu.edu.tr/mailman/admin/ LIST-NAME /members address is used.

At the membership list interface (http://mailman.metu.edu.tr/mailman/admin/LIST-NAME/members/list):- search can be performed according to the e-mail address of the member.
- On the membership table, the settings for each member of the list can be changed.   unsub is used to delete the membership.   mod is for deciding whether the messages from the member will be checked or not.    hide is to make the address of the member unseen on the membership list.    nomail is used for the member to be forbidden to receive messages due to various reasons:      U - this option may be selected according to the member's personal choice.      A - this option is at the administrator's discretion.       B - this option is selected by the system if there is a recurring problem in the user's address.      ? - state, at which the reason is unknown.   ack (acknowledgement) with this, the members are informed about the messages they have sent.   not metoo (do not send my message to me) with this, a copy of the message that the member has sent is prevented to reach his/her address.   nodupes (send no duplicates) with this, more than one copy of a message to be sent to the member is prevented.   digest (in batch) with this, the member is addressed the messages in batch (if not chosen, messages arrive one by one).    plain (plain text) with this, the messages of members who prefer in batch are made to be text only (if not selected, messages arrive in MIME format).   language (language of communication) with this, the user's language preference is made.


At the mass subscriptions interface (http://mailman.metu.edu.tr/mailman/admin/LIST-NAME/members/add):- As well as adding members to the list simultaneously, invitations to prospect members can be made.

At the mass removals interface (http://mailman.metu.edu.tr/mailman/admin/LIST-NAME/members/remove):- Removing one or more than one member is made at the field by reserving a line for a member or by downloading from an address list file.
(e) The settings for receiving the messages sent to the list as a bulk or one by one:

If it is preferred to receive messages, sent to the list, one by one, the necessary settings are selected at the interface at the address http://mailman.metu.edu.tr/mailman/admin/LIST-NAME/nondigest by selecting the "Non-digest options". At this interface there also exists a field to edit or delete the information added at the beginning or the end of the message. Normally, the below information is added at the end of each list message:

LIST-NAME mailing listLIST-NAME@metu.edu.trhttp://mailman.metu.edu.tr/mailman/listinfo/LIST-NAME If required, the information can be deleted or edited. Normally an info is not added at the beginning of the message.


If it is preferred to receive messages, sent to the list, in BULK, the necessary settings are selected at the interface at the addresshttp://mailman.metu.edu.tr/mailman/admin/LIST-NAME/digest by selecting the "Digest options". At this interface operations like, deciding at what intervals the bulk messages would be sent, arranging the information to be added at the beginning or the end of the bulk message, and adjusting the maximum message length in order to be able to send a bulk message.

(f) Arranging the privacy:

Privacy settings that might be necessary during subscription(http://mailman.metu.edu.tr/mailman/admin/LIST-NAME/privacy/subscribing):- For the list in consideration to show up when lists in the scope of mailman is inquired, the "Yes" option at the screen "Advertise this list when people ask what lists are on this machine?" should be selected.- To block membership of some e-mail addresses, which are not wanted, to the list in consideration, their e-mail addresses are listed on the field "List of addresses which are banned from membership in this mailing list." - The permission to see the list of members of a list may be given to all, only to the list members, or the administrator, from the field "Who can view subscription list?" by selecting the appropriate setting.- If it is preferred not to display the e-mail addresses of the members as e-mail addresses, the option "Yes" is selected on the field "Show member addresses so they're not directly recognizable as email addresses?".e.g. test at metu.edu.tr instead of test@metu.edu.tr.


Settings that may be necessary for privacy when sending messages(http://mailman.metu.edu.tr/mailman/admin/LIST-NAME/privacy/sender):At this interface, settings are arranged to facilitate whether to supervise messages, sent to the list, from members as well as non-members, if the messages are supervised what action to take under what circumstances and what messages to send to the users.


To set the SPAM filter(http://mailman.metu.edu.tr/mailman/admin/LIST-NAME/privacy/spam): At this interface, settings are made to decide on what action to take (delay, reject, approve etc.) when a spam identified message arrives and to filter the addresses that send spam, there is also a field where rules in various formats can be entered.e.g.from: list@listme.com (filter the messages arriving from friend@public.com address)from: .*@uplinkpro.com (filter the incoming messages with the uplinkpro.com extension)

(g) Dealing with errors and problems(http://mailman.metu.edu.tr/mailman/admin/LIST-NAME/bounce):

After how many problems will the membership of members with address problems be ended is decided with writing a number to the field, "The maximum member bounce score before the member's subscription is disabled."


Even if the address problems of the member address is eliminated after how many days would it be assumed to have recovered is entered in the field, "The number of days after which a member's bounce information is discarded, if no new bounces have been received in the interim."


After how many alert messages of "Your Membership Is Disabled" will the membership be deleted is indicated at the "How many Your Membership Is Disabled warnings a disabled member should get before their address is removed from the mailing list." field by entering a number.


The daily frequency of "Your Membership Is Disabled" alert messages is decided upon writing the day number in the field, "The number of days between sending the Your Membership Is Disabled warnings."

(h) Settings for archiving(http://mailman.metu.edu.tr/mailman/admin/LIST-NAME/archive): The settings for whether to keep an archive for the list, whether the archive be accessed by all, and the frequency of archiving are done at this interface.
(i) Settings for associating with news groups(http://mailman.metu.edu.tr/mailman/admin/LIST-NAME/gateway): The settings on this interface must be selected when the messages that are sent to the list need to be associated with some news groups.
(j) Settings for auto-reply(http://mailman.metu.edu.tr/mailman/admin/LIST-NAME/autoreply): Settings would be done at this interface when it is necessary to respond automatically for various occasions.
(k) Settings for content filtering(http://mailman.metu.edu.tr/mailman/admin/LIST-NAME/contentfilter):Settings must be done at this interface if it is needed to filter messages sent to the list with certain attachment file extensions or MIME types. When filtering is done, the action to take (sending the message excluding the attachment, refusing, approving, delaying the message) is also selected from this interface. Lists are defined to filter or distribute some certain types of files. The types of filtered and distributed files are determined according to the usage of internet and security criteria.
(l) Settings for the topic filter(http://mailman.metu.edu.tr/mailman/admin/LIST-NAME/topics):The settings for devising certain topic categories for the correspondence in a list and the list members receiving their messages according to these topics are arranged in this section. Generally, topic filter of a list is off.(m) Approval/disapproval of messages waiting to be inspected(http://mailman.metu.edu.tr/mailman/admindb/LIST-NAME): If the list is a moderated one, the messages sent to the list are saved for the inspection of the moderator to be approved or disapproved. The list moderator checks the incoming messages from this interface and decides on approving, refusing or delaying these messages.
(n) The link to the general list information(http://mailman.metu.edu.tr/mailman/listinfo/LIST-NAME): The general informative page accessible to all, can be accessed from this link on the list administrator interface.
(o) Editing the web pages and files of text accessible to all(http://mailman.metu.edu.tr/mailman/edithtml/LIST-NAME): From this interface, the public general informative web page related to the list, the web page that shows the result of the membership application, the web page that displays personal settings for the list, and the contents of the welcoming message to the new members can be edited by accessing the source codes.
(p) List archives can be reached at the link, http://mailman.metu.edu.tr/mailman/private/LIST-NAME if an archive is kept.
(r) Logging out of the list administration interface: Since the list administrator has reached the interface using a password, it is essential that he/she logs out clicking the link "Logout" due to reasons of security.






Link: https://faq.cc.metu.edu.tr/faq/how-can-i-use-mailman-interface-list-administrator

---

## Entry 2813

Question: How can I use MAILMAN Interface as a List Member? 
Answer: 

This page supplies information on how to make use of the Mailman software in order to benefit from the list services provided for people who are list members. Mailman software provides web interfaces produced in various languages, specifically in Turkish and in English, to be used with electronic list services. Assuming that the list users would primarily use the Turkish web interface, section titles and information messages on this page are given in Turkish.
To access the information about the list you are a member of:
(1) From the address http://mailman.metu.edu.tr/mailman/listinfo click on the list you are a member of.
(2) On the window that comes up as the address http://mailman.metu.edu.tr/mailman/listinfo/LIST-NAME you can access the information or perform the tasks below:
(a) Description of the List: If a detailed description was provided by the list administrator, these can be accessed in the related section About LIST-NAME.
(b) Language Option: If, for a list, more than one language option is provided, the language preferred for the interface can be selected from the top, right corner of the page. If no option for the interface language is permitted, the standard language used for the interface is in Turkish.

(c) List archive: In order to browse messages that have already been sent to the list, click on the link in the sentence, "To see the collection of prior postings to the list, visit the LIST-NAME Archives." If no messages have been sent to the list yet, an alert "No messages have been posted to this list yet, so the archives are currently empty" will show up. If there are already sent messages and if the archive is open to all, they will be shown to be inquired according to different types of sorting (subject, date, sending member etc.)
(d) List address: In order to send a message to the list an address similar to LIST-NAME@metu.edu.tr must be entered.
(e) List Membership application: You can apply to a list, you are not a member of, by filling in your name and your e-mail address in the relevant parts under the section Subscribing to LIST-NAME and sending it:

After filling in your name and your e-mail address, it is necessary for you to decide on a password you would need to use the list. If you do not indicate a password, one will automatically be assigned to you and be sent to you in the body of the message that will be sent to confirm your membership.
You can also select the language you would prefer to use for correspondence in the same area.

If you want to receive the messages sent not one by one but as a daily batch, the option below must be selected asYes.

After entering all of the above you can click on the,

button and complete your membership application.
(f) Seeing the list of the members, to unsubscribe or change membership settings: If the list settings were made to facilitate to see the other list members, by entering your e-mail address you have given during your application and your password you can see a list of the members:

To unsubscribe or change your list membership settings you have to enter your e-mail address:




Link: https://faq.cc.metu.edu.tr/faq/how-can-i-use-mailman-interface-list-member

---

## Entry 2814

Question: How the size of the messages sent to the list can be limited?
Answer: 

To limit the size of the messages sent to the list:
(a) The value of the message size that could be sent including the attachment is entered at the field General Options> Additional settings > Maximum length in kilobytes (KB) of a message body. Use 0 for no limit in units of KB. If the value is zero (0) there would be no limit to the message size.


Link: https://faq.cc.metu.edu.tr/faq/how-size-messages-sent-list-can-be-limited

---

## Entry 2815

Question: I am a member of "abc-l" list but I can not receive the messages sent to the list anymore. What may be the problem? (in Turkish)
Answer: 

Önceden mesajları alabiliyorken, belli bir tarihten sonra alamamaya başladıysanız kullanıcı hesabınızın ve/ya liste üyeliğinizin ayarlarında değişiklik meydana gelmiş olabilir. Liste üyelik durumunuzu kontrol için abc-l-ownermetu.edu.tr adresinden liste yöneticisiyle iletişime geçerek liste üyelik durumunuzu, üyeliğinizin dondurulup dondurulmadığını kontrol ediniz.
Liste ayarları ile ilgili bir sorun yoksa kullanıcı hesabı ayarlarınızda farklı bir düzenleme gerçekleşmiş olabilir (yönlendirme, mesaj kutunuzun dolması, spam ayarlarında değişiklik vb.) Kullanıcı hesabı ayarlarınızın kontrolü için e-posta hizmeti aldığınız kurumun yetkilileriyle iletişime geçmeniz gerekmektedir. E-posta adresiniz kullanici_adimetu.edu.tr şeklindeyse https://bilisimdestek.metu.edu.tr adresi üzerinden bizimle iletişime geçebilirsiniz.
(Yukarıda geçen "abc-l" ifadesi liste ismi için örnek olarak verilmiştir).


Link: https://faq.cc.metu.edu.tr/faq/i-am-member-abc-l-list-i-can-not-receive-messages-sent-list-anymore-what-may-be-problem-turkish

---

## Entry 2816

Question: I am a member of "xyz-l" list. I  clicked on the password reminder button to obtain my list membership password; but  I did not receive the password yet. Is there something wrong? (in Turkish)
Answer: 

Büyük olasılıkla girdiğiniz e-posta adresi listeye üye bir adres değildir. E-posta adresinizle listeye üye olmadiğınız halde liste mesajlarını alıyorsanız bunun sebebi mesaj yönlendirme olabilir. Yani eğer mesajlarınızı birden fazla e-posta adresi ile takip ediyor ve bu adresler arasında yönlendirme kullanıyorsanız, liste mesajlarının gönderildiği e-posta adresiniz ile listeye üyelik için kullandığıniz e-posta adresi farklı olabilir. Bu konuyla ilgili olarak listenin yöneticisiyle görüşebilirsiniz.
Liste yöneticisinin e-posta adresini bilmiyorsanız xyz-l-ownermetu.edu.tr adresinden liste yöneticisine ulaşabilirsiniz.
(Yukarıda geçen "xyz-l" ifadesi liste ismi için örnek olarak verilmiştir)


Link: https://faq.cc.metu.edu.tr/faq/i-am-member-xyz-l-list-i-clicked-password-reminder-button-obtain-my-list-membership-password-i

---

## Entry 2817

Question: I am a METU personnel but I can not receive the messages from university administration sent to announcement lists. What should I do? (in Turkish)
Answer: 

Üniversitemiz yönetimince mensuplarımız için çeşitli duyuru listeleri tanımlanmıştır. Öğrencilerin, akademik ve idari personelin kendileriyle ilgili bu listelere üyelikleri bir otomasyonla sağlanmaktadır. 
Bu liste(ler)e gönderilen mesajlari daha önce görüyor ancak bir süredir göremiyorsaniz mailmanmetu.edu.tr adresine ilgili listeye üyelik için kullandığınız e-posta adresinden durumu bildiren bir e-posta gönderiniz. Üyelik durumunuz incelenecek, konu hakkında size bilgi verilecektir.
Eğer ilgili listelerden şimdiye kadar hiç e-posta almadıysanız üyelik başvurusunda bulunmanız gerekmektedir. Bu konuda "Bir listeye üye olmak için ne yapmalıyım?" bölümünden bilgi alabilirsiniz.


Link: https://faq.cc.metu.edu.tr/faq/i-am-metu-personnel-i-can-not-receive-messages-university-administration-sent-announcement-lists

---

## Entry 2818

Question: I am a METU student; can I subscribe to "genel-duyuru" list? (in Turkish)
Answer: 

"genel-duyuru" listesine ODTÜ personeli olan kisiler kullanici_adimetu.edu.tr seklindeki e-posta adresleri ile otomatik olarak kaydedilmektedir. Ögrencilerin üyelik talepleri kabul edilmemektedir.
Üniversite Rektörlüğünce Öğrencilere yönelik "a-ogrenci-duyuru" (Ankara ve Erdemli Kampusu öğrencilerine yönelik) ve "ogrenci-duyuru" (Ankara, Erdemli ve Kıbrıs Kampusu öğrencilerine yönelik) listeleri bulunmaktadır. 


Link: https://faq.cc.metu.edu.tr/faq/i-am-metu-student-can-i-subscribe-genel-duyuru-list-turkish

---

## Entry 2819

Question: I am member of "abc-l" list but the messages I send does not arrive to the list. What may be the problem? (in Turkish)
Answer: 

Eğer söz konusu liste "tek yönlü duyuru listesi" ise, liste yapılandırması gereği e-posta gönderme yetkisine sahip kişiler haricinde hiç bir kullanıcı mesaj gönderememektedir. Ancak üyelerin e-posta gönderebildiği bir liste söz konusu ise, gönderdiginiz mesajlarin listeye ulaşmamasının iki temel sebebi vardır:
Listeye üyelik için kullanmadığıniz bir e-posta adresinden mesaj gönderiyor olabilirsiniz. Genelde birden fazla e-posta adresi kullanıyorsanız ve üye olan adresten farklı bir adrese yönlendirme tanımladıysanız, liste mesajlarini aldığınız e-posta adresi ile üyelik için kullandığınız e-posta adresi farklı olabilir. Mesajları aldığınız e-posta adresinin listeye üye olarak kayıtlı olup olmadığını kontrol etmesi için abc-l-ownermetu.edu.tr adresinden liste yöneticisiyle iletişime geçiniz.
Listeye üyelik için kullandığınız e-posta adresinden mesaj gönderiyorsanız mesajiniz onay bekliyor olabilir. Mesajinızın onay için bekletiliyor olmasının olası sebepleri aşağıda listelenmiştir:
Gönderdiğiniz mesaj liste mesaj kotasını aşan bir büyüklüğe sahip olabilir (örneğin; çok büyük bir dosya eklentisi gönderiyor olabilirsiniz).
Mesajınızın alıcı adresi bölümünde liste adıyla beraber çok sayıda e-posta adresini yazmış olabilirsiniz.
Mesajiniz liste ayarları gereği moderatör onayı için bekletiliyor olabilir.
Tüm bu olası sebeplerle ilgili olarak abc-l-ownermetu.edu.tr adresinden liste yöneticisi ile iletişime geçebilir, detaylı bilgi alabilirsiniz.

(Yukarıda geçen "abc-l" ifadesi liste ismi için örnek olarak verilmiştir)


Link: https://faq.cc.metu.edu.tr/faq/i-am-member-abc-l-list-messages-i-send-does-not-arrive-list-what-may-be-problem-turkish

---

## Entry 2820

Question: I am the administrator of  "abc-l" list. I do not remember the list admin password. How can I get it? (in  Turkish)
Answer: 

Liste yönetim şifresini edinmek için listenin yöneticisi olarak kullandığınız e-posta adresinden mailman@metu.edu.tr adresine yöneticisi olduğunuz listenin adı ve telefon numarası bilginizi vererek şifre isteğinizi bildiren bir e-posta gönderiniz. E-Liste servis yöneticisi talebiniz üzerine gerekli incelemeleri gerçekleştirecek, talebin uygun görülmesi durumunda sizinle telefon aracılığıyla iletişime geçecektir.
E-Liste yöneticiliğinde bir değişiklik söz konusu olduğunda, önceki e-liste yöneticisi yeni liste yöneticisinin e-posta adresini listenin yönetim arayüzü üzerinde yönetici olarak tanımlamalı ve yönetim şifresini yeni yöneticiye teslim etmelidir. Ancak, liste yöneticisinin yeni yöneticiyi tanımlamadan ve şifreyi aktarmadan görevden ayrılması gibi durumlarda, farklı bir kişinin liste yöneticisi olarak tanımlanmasına BİDB tarafından destek verilebilmektedir.
Böyle bir durum söz konusu ise, ilgili listenin yeni yöneticisi olacak kişinin konuyla ilgili talebini "metu.edu.tr" uzantılı e-posta adresini kullanarak mailmanmetu.edu.tr adresine iletmesi gerekmektedir. Söz konusu liste üniversitedeki bir birime ait ise, bu talep ilgili birimin yöneticisi tarafından iletilmelidir. Talebin BİDB'na ulaşmasının ardından, talep sahibi ile iletisime geçilerek gerekli işlemler gerçekleştirilecektir.
(Yukarıda geçen "abc-l" ifadesi liste ismi için örnek olarak verilmiştir.)


Link: https://faq.cc.metu.edu.tr/faq/i-am-administrator-abc-l-list-i-do-not-remember-list-admin-password-how-can-i-get-it-turkish

---

## Entry 2821

Question: I am the administrator of "abc-l" list. Can I change the name of the list? (in Turkish)
Answer: 

Mailman sisteminde liste isim degişikliği teknik olarak mümkün değildir. Bu amaca yönelik talep gelmesi durumunda "xyz-l" listesi açılır, "abc-l" listesinin üye ve yapılandırma bilgileri "xyz-l" listesine aktarılır. Talep edilmesi durumunda "abc-l" arşivi de "xyz-l" listesine kopyalanır. Ancak arşiv aktarımında sorun yaşanmaması ile ilgili bir garanti verilmemektedir.
(Yukarıda geçen "abc-l" ve "xyz-l" ifadeleri liste ismi için örnek olarak verilmiştir.)


Link: https://faq.cc.metu.edu.tr/faq/i-am-administrator-abc-l-list-can-i-change-name-list-turkish

---

## Entry 2822

Question: I do not want to receive messages from university administration via genel-duyuru etc. What can I do? (in Turkish)
Answer: 

Üniversitemiz yönetimince mensuplarımız için çeşitli duyuru listeleri tanımlanmıştır. Öğrencilerin, akademik ve idari personelin bu listelere üyelikleri bir otomasyonla sağlanmaktadır. Bu sebeple üyelikten çıkış taleplerine yönetim kararı uyarınca izin verilmemektedir.


Link: https://faq.cc.metu.edu.tr/faq/i-do-not-want-receive-messages-university-administration-genel-duyuru-etc-what-can-i-do-turkish

---

## Entry 2823

Question: I have forgotten the password of an electronic list that I have subscribed, how can I get it? (in Turkish)
Answer: 

E-listelerde kullanılan üyelik şifreleri, merkezi kullanıcı kodları için kullanılan şifrelerden farklı olup, herhangi bir listeye üye olunduğunda Mailman yazılımı tarafından otomatik olarak tanımlanıp e-liste üyelerine gönderilen şifrelerdir. E-liste servisi kapsamında merkezi e-posta adresleri dışındaki e-posta adresleri ile de e-listelere üye olunabildiği için, e-liste arşivlerine ulaşımda merkezi kullanıcı şifreleri kullanılamamaktadır.
E-liste şifresini hatırlamayan bir kullanıcı, bir e-listeye gönderilmiş mesajın ekinde yer alan eklenti dosya bağlantısına tıkladığında veya doğrudan http://mailman.metu.edu.tr/mailman/private/liste_adi şeklindeki e-liste arşiv giriş ekranının adresini yazarak, arşive giriş yapacağı sayfaya ulaşabilir. E-liste şifresini öğrenmek için, bu sayfada e-listeye üyelik için kullandığı e-posta adresini yazıp _x0093_Hatırlat_x0094_ butonuna basması yeterlidir.

Bu işlem sonrasında e-liste şifresi kullanıcının e-posta adresine aşağıdaki gibi bir mesaj ile gönderilecektir:

Burada, "Your <e-liste-adı> password is:" ifadesinin karşısında "****" ile belirtilmiş olan alanda yer alan bilgi, e-liste şifre bilgisidir. Kullanıcı bu şifreyi kullanarak mesaj ekinde yer alan eklenti dosyalara ulaşabilir ve e-liste arşivinde yer alan geçmiş tüm mesajları okuyabilir (E-liste yazılımı olan "Mailman", üye olunan her liste için ayrı şifre atamaktadır, ancak isteyen kullanıcılarımız üye oldukları tüm listeler için ortak bir şifre tanımlayabilirler).


Link: https://faq.cc.metu.edu.tr/faq/i-have-forgotten-password-electronic-list-i-have-subscribed-how-can-i-get-it-turkish

---

## Entry 2824

Question: I have subscribed to "abc-l"  list with my e-mail address name_surname@domain. Can I change my subscription address without making any  unsubscription-resubscription operations? (in Turkish)
Answer: 

Liste üyeliğinden çıkmadan sadece üyelik adresinizi değiştirmeniz mümkündür. Bunun için;
http://mailman.metu.edu.tr/mailman/listinfo/abc-l adresinde sayfanın en altında yer alan "Listeden çık veya seçeneklerimi düzenle" yazılı alana listeye üyelik için kullandığınız e-posta adresi ile giriniz.
http://mailman.metu.edu.tr/mailman/options/abc-l adresinde sayfanın üst kısmına listeye üyelik şifrenizi giriniz (Eğer üyelik sifrenizi bilmiyorsanız aynı sayfada yer alan "Hatırlatıcı"yı kullanabilirsiniz). Konu hakkında daha detaylı bilgi için http://faq.cc.metu.edu.tr/faq/i-have-forgotten-password-electronic-list-i-have-subscribed-how-can-i-get-it-turkish adresinden yararlanabilirsiniz.
Sayfanın en üst alanında "üyelik bilgilerinin değişimi" kısmından üyelik için kullandığınız adresinizi değiştirebilirsiniz. Üyelik adresinizi Mailman sistemi altındaki tüm listeler için değiştirmek isterseniz "Adresimi ve ismimi değiştir" butonunun altında yer alan "Global olarak değiştir" seçeneğini işaretlemelisiniz.
(Yukarıda geçen "abc-l" ve "ad_soyaddomain" ifadeleri liste ismi ve e-posta adresi için örnek olarak verilmiştir)


Link: https://faq.cc.metu.edu.tr/faq/i-have-subscribed-abc-l-list-my-e-mail-address-namesurnamedomain-can-i-change-my-subscription

---

## Entry 2825

Question: I'd like to receive the messages  sent to a list in a digest format. How can I change my subscription options? (in Turkish)
Answer: 

Liste mesajlarını listeye ileti gönderildikçe değil de toplu olarak almak isterseniz aşağıda yer alan işlem adımlarını takip edebilirsiniz:
http://mailman.metu.edu.tr/mailman/listinfo/abc-l adresinde sayfanın en altında yer alan "Listeden çık veya seçeneklerimi düzenle" yazılı alana listeye üyelik için kullandığınız e-posta adresi ile giriniz.
http://mailman.metu.edu.tr/mailman/options/abc-l adresinde sayfanin üst kısmına listeye üyelik şifrenizi giriniz (Eğer üyelik sifrenizi bilmiyorsanız aynı sayfada yer alan "Hatırlatıcı"yı kullanabilirsiniz).
Gelen sayfanın alt kısmında yer alan ayarlardan "Toplu Mesaj Modunu Ayarla" bölümünü "Açık" olarak işaretleyerek mesajlarınızı toplu almaya başlayabilirsiniz.
(Yukarıda geçen "abc-l" ifadesi liste ismi için örnek olarak verilmiştir)


Link: https://faq.cc.metu.edu.tr/faq/id-receive-messages-sent-list-digest-format-how-can-i-change-my-subscription-options-turkish

---

## Entry 2826

Question: What are the settings to keep an archive of the list?
Answer: 

The settings to keep an archive of the list:
(a) If the list is not to be archived, the setting at Archiving Options > Archive messages? is selected as NO.(b) If the list is to have an archive but only to be seen by the list members:    (b1) The setting at Archiving Options > Archive messages? is selected as YES.    (b2) The setting at Archiving Options > Is archive file source for public or private archival? is also selected as YES.


Link: https://faq.cc.metu.edu.tr/faq/what-are-settings-keep-archive-list

---

## Entry 2827

Question: What should I do to subscribe to a list? (in Turkish)
Answer: 

Üyelik basvurusu için http://mailman.metu.edu.tr/mailman/listinfo/abc-l/ adresinde yer alan "abc-l Listesine Üyelik" bölümündeki formu doldurunuz. Başvurduğunuz listenin üyelik tercihlerine bagli olarak üyeliginiz gerçekleşir, onay sürecine girer ya da reddedilir.
Liste üyelik islemleri listelerin yöneticileri tarafından yürütülmektedir. Üyelik tercihleri de liste yöneticileri tarafından belirlenmektedir. Gerekli durumlarda abc-l-ownermetu.edu.tr adresinden söz konusu listenin yöneticisi ile iletisime geçebilirsiniz.
(Yukarıdaki URL ve e-posta adreslerinde geçen "abc-l" ifadesi örnek olarak verilmiştir. "abc-l" yerine üye olmak istediğiniz listenin adını yazmalısınız.)


Link: https://faq.cc.metu.edu.tr/faq/what-should-i-do-subscribe-list-turkish

---

## Entry 2828

Question: Bölüm, Birim, Merkez, Laboratuvar, Öğrenci Topluluğu web sayfası nasıl yapılır?
Answer: 

Sayfanız için bir web hesabı ve alan adı gerekecektir. Bunun için https://cc-form.metu.edu.tr/web adresinde yer alan "Yeni Web Kullanıcı Kodu ve Alan Adı Başvuru Formu"nu doldurmanız gerekmektedir. Başvurunuz üzerine sizinle iletişime geçilecektir. Web sitenizi aşağıdaki yöntemlerden biri ile oluşturabilirsiniz.
Kendiniz Dreamweaver ya da benzeri bir programla web sayfalarınızı hazırlayabilirsiniz. 
Merkezi İçerik Yönetim Sistemi'ni (MİYS) kullanabilirsiniz. MİYS açık kaynaklı bir içerik yönetim sistemi olan Drupal alt yapısını kullanmaktadır. Üniversitemizdeki akademik bölüm, idari birim, merkez, enstitü, fakülte/yüksekokul, lisansüstü program, laboratuvar, proje/araştırma grubu, öğrenci topluluğu vb. yapılara ait web sayfaları bu sistem üzerinde oluşturulabilmektedir. MİYS ile ilgili ayrıntılı bilgiye ve başvuru formuna http://miys.metu.edu.tr adresinden erişebilirsiniz. Bu sistemi kullanırsanız MİYS kapsamında geçerli görsel kimlik standartlarına (http://www.metu.edu.tr/tr/gkk/gorsel-kimlik-standartlari) uymanız beklenmektedir.
ODTÜ Blog Servisi'ni kullanabilirsiniz. ODTÜ Blog Servisi, özgür bir yazılım olan WordPress altyapısını kullanmaktadır. Bu servis ile üniversitemizdeki akademik bölüm, idari birim, merkez, enstitü, fakülte/yüksekokul, lisansüstü program, laboratuvar, proje/araştırma grubu, öğrenci topluluğu vb. yapılara ait web siteleri kapsamlı bir şekilde hazırlanabilir, bu sitelerde çeşitli yazılar ve sayfalar oluşturulabilir. Tasarım için biraz daha esnek olsa da serviste yer alan şablonlar dışında kalan harici bir şablona onay verilmemektedir. Servise giriş yapmak ve servis hakkında ayrıntılı bilgi almak için http://blog.metu.edu.tr adresi kullanılmalıdır.
 

Link: https://faq.cc.metu.edu.tr/faq/bolum-birim-merkez-laboratuvar-ogrenci-toplulugu-web-sayfasi-nasil-yapilir

---

## Entry 2829

Question: How can I change the file and directory permissions in Unix operating system with the 'chmod' command?
Answer: 

In the Unix operating system, "ls" command displays the names of directories and file names. The user can also view the files according to his/her preferences from among some command options.
-a
Displays all the content of the directory including the hidden files beginning with '.'
-l
Lists files and gives details about them(date of last process, file permissions )
-t
Lists the files according to the dates when these files are last modified.
-R
Lists all the files including the contents of subdirectories.
In Unix, there are file permissions like read, write and execute for three categories of users, namely, file owner, group and others. The file permissions that are assigned to a file can be displayed with "ls -l" command.
 
bash-2.03$ ls -ltotal 100-rw------- 1 usrname usrgrp 1156 Nov 29 14:30 a_file-rw-r--r-- 1 usrname usrgrp   11 Dec 19 17:29 file1drwx------ 2 usrname usrgrp  512 Nov 29 14:44 maildrwxr-xr-x 5 usrname usrgrp  512 Nov 29 11:56 wwwhome
 
A closer look at the screen above will show that there are seven basic columns.
1
2
3
4
5
6
7
drwxr-xr-x
5
username
usergroup
512
Nov 29 11:56
wwwhome
1st Column This column shows the read, write and execute permissions of wwwhome directory. It includes 10 characters.
 
The first character in the permission sequence "drwxr-xr-x" can be "-", "d" or "l" and these characters simply signify "file", "directory" and "link" respectively.
The remaining nine characters are grouped three by three. The first group signifies the owner's permissions, the second group signifies the group's permissions and the third group signifies other users' permissions.
The three characters in these three groups signify respectively the read, write and execute permissions of all categories of users.

2nd Column; This column displays the number of links that are working in a file. The number of links for a directory indicates the total of links present in this directory and the directories linked to this directory.
3rd and 4th Columns; This column displays the user code and the group which the user belongs to,
5th Column; This column displays the size of the file or the total character number reserved for a file,
6th Column; This column displays the date when the last modification on the directory took effect,
7th Column This column displays the name of the directory or file.
The read, write and execute permissions are specified or modified solely by the owner of the file. The permissions assigned to a file can be modified buy the "chmod" command. The command sequence is as follows;
chmod [permissionmode] [filename]

Permission mode is comprised of the category characters, permit/prohibittance characters and the characters showing type of the permission. '+' sign gives file permissions, '-' sign omits the file permission. The file name is the name of the file whose file permissions would be changed. For example:
bash-2.03$ chmod go-x wwwhome   1bash-2.03$ ls -l wwwhome        2total 102drwxr--r-- 2 username usergroup 512 Nov 29 11:56 wwwhome
"chmod go-x" command is executed for the "wwwhome" directory on line 1 in the above example. In the second line, "ls -l"command checks the permissions of "wwwhome" directory. Apparently, no one other than the owner is permitted to write into and execute "wwwhome" any longer.


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-change-file-and-directory-permissions-unix-operating-system-chmod-command

---

## Entry 2830

Question: I forgot the web user account's password, How can I learn it?
Answer: 

If you forget the web user account's password, you should follow the procedures written at http://faq.cc.metu.edu.tr/faq/i-forgot-my-password-where-can-i-apply
For the web accounts in the format of www*****, recovery e-mail address is the user code of the responsible staff of the account. Responsible staff for the web accounts of student clubs is the academic advisor of the club. 
If you have any problems regarding password of web account, you may contact with webadminmetu.edu.tr address. 
 


Link: https://faq.cc.metu.edu.tr/faq/i-forgot-web-user-accounts-password-how-can-i-learn-it

---

## Entry 2831

Question: What are the Required and Suggested Content Features for the Web Pages of Academic/Administrative Units and Student Clubs
Answer: 

Required features
Suggested features
Suggested content structure for academic departments
Suggested content structure for administrative departments
Suggested content structure for student clubs

1. Required featuresAll department and club web pages should have the features mentioned below:

Main page and/or sub-pages of Unit/Club web sites should provide a link to METU home page (http://www.metu.edu.tr or http://www.odtu.edu.tr)


Main page and/or sub-pages of Unit/Club web sites should provide contact information (at least an e-mail address and a telephone number if possible) for the people who wish to send their comments, suggestions or ask questions.


All pages should be checked and updated regularly (for instance, in order to remove out-of-date information and broken links). For those pages which are frequently updated, an indication of  "the last update" date is recommended.

2. Suggested featuresWhile department and club web pages are being designed and prepared, the following details should be taken into account:

Department/club web pages are kept on web accounts which have limited quotas. In order to make efficient use of the account quota, the unnecessary files, which exist in the reserved space of web accounts, should be removed and the file sizes should be adapted for web usage. In order to provide accessibility, images, text, documents, etc. should be adapted for web environment (e.g., images should be optimized for web, big files should be compressed or font size of textual information should be chosen appropriately to make it legible.)
It is advantageous to prepare the web documents by web editors and "Save as Web Page" option of MS Word program should not be preferred for this purpose. If it is really necessary, the file type to be created should be selected as "Filtered Web Page" and the generated source code should be cleaned up as much as possible (i.e. unnecessary tags should be removed.)
If the web pages include any text or multimedia items provided from external sources, their sources (web page address, publication etc.) should be indicated.
Web page content and design should be prepared in accordance with METU Information Technology Resources Use Policy.
Both English and Turkish versions of the web page content should be prepared, if it addresses international users.

3. Suggested content structure for academic departmentsAcademic departments may benefit from the below content structure while preparing their web pages:

Short information (such as the main features of the department that distinguishes it from other departments in other universities, ...)
General information (department history, future plans and studies, facilities, ...)
Programs (undergraduate/graduate curriculum, description of courses, courses offered, course schedule, ...)
Department staff (information including name, title, address, phone, e-mail, research fields etc. for the department staff)
Students (student lists, student groups, ...)
Research (facilities, groups, projects, centers, studies at department, ...)
Publications (books, journals, ...)
Announcements (activities as seminars and conferences, public announcements, ...)
References and Resources (i.e. FTP Site, web mirrors, links, ...)
4. Suggested content structure for administrative departmentsAdministrative departments may benefit from the below content structure while preparing their web pages:

Mission and vision, a short history of the department/unit
Organization (sub-units, organization scheme, ..)
Department staff (information including name, title, address, phone, e-mail etc. for the department staff)
Services offered (detailed information about services, how the users can make use of these services, ...)
Announcements (announcements about services, public announcements, ...)

5. Suggested content structure for student clubsStudent clubs may benefit from the below content structure while preparing their web pages:

Mission and short history (reasons for the existence of the club, how it was established, ...)
Activities (activities organized by the club or other related institutions, ...)
Club members (organization scheme, working groups, ...)
Announcements (activity announcements, public announcements, ...)
Related links (similar clubs in other universities, related institutions, ...)



Link: https://faq.cc.metu.edu.tr/faq/what-are-required-and-suggested-content-features-web-pages-academicadministrative-units-and

---