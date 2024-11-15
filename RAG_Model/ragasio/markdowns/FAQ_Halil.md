# FAQ_Halil

## Entry 2512

Question: How can I connect to eduroam wireless network using my Windows 10 computer?
Answer: 

If you are using Windows 10, then you do not need to install a program.
In the list of wireless networks, please select eduroam and use your usercode and password to connect. Do not forget to add @metu.edu.tr to the usercode (like username@metu.edu.tr)


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-connect-eduroam-wireless-network-using-my-windows-10-computer

---

## Entry 2513

Question: How can I connect to meturoam network?
Answer: A device must support WPA2 Enterprise with PEAP/MSCHAPv2 in order to be able to connect to METU wireless network, meturoam. Please click here: https://faq.cc.metu.edu.tr/faq/which-devices-are-known-not-support-meturoam for a list of some popular devices that are known to NOT work on the meturoam wireless network.
To connect to the meturoam wireless network, you need a METU usercode and a password for meturoam. If you have a password, please continue to HOW-TO  section.
If you didn't create a password for meturoam or you want to renew your password, please visit https://netregister.metu.edu.tr and click Wireless icon, then click "meturoam" icon.

In the meturoam menu, please provide a new password to be used only for this service with your user code. (In some Android and IOS devices, some special characters like #, ', $ in the password may cause problems to connect to meturoam. If you can connect to meturoam via a computer but having problems with Android or IOS devices, please check your password for special characters and create a new password with other characters.)

 
Connecting to meturoam
After you set your new password, please connect to meturoam SSID from your wireless device. You can use this password with every device you own, you do not have to set passwords for each device.
Be sure to set the protocols as PEAP and MSCHAPv2. 
Use your METU usercode and password for the meturoam service. (Please make sure you use your usercode like e123456metu.edu.tr, not your email aliases in the form of name.surnamemetu.edu.tr)
In Windows 10, protocol settings are done automatically. You do not need to set the protocols. For Linux operating systems or Windows 7 and below, you may also need to select WPA2-Enterprise and AES.
In mobile devices, if you use the autocomplete function in your keyboard, a blank space may be added to your usercode. Pay attention to last character in your usercode. It should not be a blank space.
If you are asked for a certificate, you may select "Do not validate" and skip it. (For some Android devices, certificate field might be compulsory. You can select "Use System Certificate" and type border.metu.edu.tr netlogin.metu.edu.tr)
If you are asked for anonymous identity, you may type anonymous@metu.edu.tr.

For Raspberry pi devices, add the following conf to wpa_supplicant.conf file.network={ssid="meturoam"key_mgmt=WPA-EAPpairwise=CCMPeap=PEAPidentity="< username >"anonymous_identity="anonymous@metu.edu.tr"password="< password >"}
Then restart wpa_supplicant. Actual filenames and paths may vary.killall wpa_supplicantwpa_supplicant -B -Dwext -i wlan0 -c /etc/wpa_supplicant/wpa_supplicant.conf -f /var/log/wpa_supplicant.log

 

 If you forgot your password, you can set a new one in order to use the wireless network.
Those users who do not prefer to create a meturoam password can also connect to eduroam.
!!! Wireless network connection problems are observed in some of Android devices using Android 6 and prior versions. Occasionally these devices display there is an established wireless connection on the screen but when you try to connect to the Internet, they fail. This problem is originated from a bug in the operating system. The bug cause Android devices to continue to use DHCP-leased IP addresses after the leases expire, and cause Android devices to resume using IP addresses from expired DHCP leases. When you face the the same problem please disable your Wi-Fi connection and enable it again.


Link: https://faq.cc.metu.edu.tr/faq/meturoam

---

## Entry 2514

Question: A guest account created for me. How can I connect meturoam wireless network?
Answer: 

A device must support WPA2 Enterprise with PEAP/MSCHAPv2 in order to be able to connect to METU wireless network, meturoam. Please click here: https://faq.cc.metu.edu.tr/faq/which-devices-are-known-not-support-meturoam for a list of some popular devices that are known to NOT work on the meturoam wireless network.
Connecting to meturoam
After a guest account created for you, please connect to meturoam SSID from your wireless device. You can use this password with every device you own, you do not have to set passwords for each device.
Be sure to set the protocols as PEAP and MSCHAPv2. 
Use your username and password sent via e-mail by the guest account creator for the meturoam service.
In Windows 10, protocol settings are done automatically. You do not need to set the protocols. For Linux operating systems or Windows 7 and below, you may also need to select WPA2-Enterprise and AES.
In mobile devices, if you use the autocomplete function in your keyboard, a blank space may be added to your username. Pay attention to last character in your username. It should not be a blank space.
If you are asked for a certificate, you may skip it. (For some Android devices, certificate field might be compulsory. You can select "Use System Certificate" and type border.metu.edu.tr netlogin.metu.edu.tr)
If you are asked for anonymous identity, you may type anonymous@metu.edu.tr.
!!! Wireless network connection problems are observed in some of Android devices using Android 6 and prior versions. Occasionally these devices display there is an established wireless connection on the screen but when you try to connect to the Internet, they fail. This problem is originated from a bug in the operating system. The bug cause Android devices to continue to use DHCP-leased IP addresses after the leases expire, and cause Android devices to resume using IP addresses from expired DHCP leases. When you face the the same problem please disable your Wi-Fi connection and enable it again.


Link: https://faq.cc.metu.edu.tr/faq/guest-account-created-me-how-can-i-connect-meturoam-wireless-network

---

## Entry 2515

Question: How can I access to The Resources of METU Library from outside of METU?
Answer: 

Important Notice !!!
Library Webcache Service was ended on 5th of August 2014. In order to access the Library Electronic Recources from outside of METU Campus please use the other services which explained in this link below:http://lib.metu.edu.tr/remote-access
 


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-access-resources-metu-library-outside-metu

---

## Entry 2516

Question: How to managed METU Departments/Units Wired Network?
Answer: For more information about METU Departments/Units Wired Network please click here: https://bidb.metu.edu.tr/en/departmentsunits-wired-network-service

Link: https://faq.cc.metu.edu.tr/faq/how-managed-metu-departmentsunits-wired-network

---

## Entry 2517

Question: I cannot make remote desktop connection, what should I do?
Answer: 

If you are having trouble setting up a remote desktop connection, it may be possible for two reasons.
a) The port number used for the connection should be changed
b) There is a problem with the remote desktop connection settings or the username

a) The port number used for the connection should be changed
Some security measures has been taken about the port 3389 which is used for remote desktop connection to METU campus. Port 3389 keeps closed two-way (campus in and out) because of security reasons. In order to connect to your computer at METU from outside the campus using remote desktop connection, you should change the remote desktop port number for both of the computers. There are two ways to do so:
Select Start > Run > regedit. On "Registry Editor" select HKEY_LOCAL_MACHINE \ System \ CurrentControlSet \ Control \ TerminalServer \ WinStations \ RDP-Tcp and change the "PortNumber" with any unused port number between 1025 and 65535.

Then, you should give permission to this port number on Windows Firewall. For Windows 7, select Control Panel > System and Security > Windows Firewall > Advanced Settings. For Windows 10, select Start > Windows Administrative Tools > Windows Defender Firewall with Advanced Security.
From the menu on the left side, select Outbound Rules on the computer you are using remote desktop connection, Inbound Rules on the computer you are going to connect remotely. Then click New Rule on the right. If you are going to use both computers to be connected remotely, you should create both inbound and outbound rules on both computers.


On "New Outbound Rule Wizard", select Port as the rule type and click Next. On the next screen choose the protocol as TCP and write down the port number you have defined.


Then, select Allow the connection and click Next. Finally, specify a name for the rule and click Finish


If you are using a firewall software other than Windows Firewall, you should give permissions to the port number on that software.
To activate the settings restart the computers. For using remote desktop connection, write down the computer name as IP:port number.

b) There is a problem with the remote desktop connection settings or the username
The username that should be entered for the remote desktop connection may not be the same as the username when computer is turned on. If you are having trouble making a remote desktop connection to your computer, it is necessary to check that the username. To do this, the you should start the Task Manager (press "Ctrl + Alt + Delete" and choose "Start Task Manager" or press right click on the taskbar and choose "Start Task Manager") and check the username on the "Users" tab.


By establishing a remote connection you should use this username.

If there is a version difference with the remote desktop connection provided between the two computers (eg, trying to connect a Windows 7 computer from a Windows XP computer), you should choose "Allow connections from computers running any version of Remote Desktop (less secure)" from the remote desktop connection settings. You could access these settings from "Remote" tab in the "System Properties".


 


Link: https://faq.cc.metu.edu.tr/faq/i-cannot-make-remote-desktop-connection-what-should-i-do

---

## Entry 2518

Question: I forgot meturoam password, what can I do?
Answer: 

Please set a new password, following the instruction on https://faq.cc.metu.edu.tr/faq/meturoam


Link: https://faq.cc.metu.edu.tr/faq/i-forgot-meturoam-password-what-can-i-do

---

## Entry 2519

Question: I get a certificate warning when connecting to the wireless meturoam network with my device. What should I do?
Answer: 

When connecting to the meturoam wireless network, you may receive a certificate warning due to the operating system on your device and the antivirus software you use, if any.
You can check the information on the alert screen and click Connect if the information is the same as the "Fingerprint" below:
Radius Server: border.metu.edu.tr
SHA-256 Fingerprint 52 FD 75 C8 9D 32 57 61 30 77 88 BA 9B 01 E0 6F F5 4C 1F 19 08 10 E5 F5 D4 F7 87 2E E4 6D A4 7A
SHA-1 Fingerprint 5A 12 B5 A2 5E 20 D1 BC 73 74 2E 0E 35 60 B5 76 3D DB 14 A7


Link: https://faq.cc.metu.edu.tr/faq/i-get-certificate-warning-when-connecting-wireless-meturoam-network-my-device-what-should-i-do

---

## Entry 2520

Question: Is there a Domain Name Service in METU?
Answer:   METU CC Network Group gives campuswide DNS service (metu.edu.tr, odtu.edu.tr, metu.edu).  METU CC DNS servers reply the queries of IP addresses that belong only to METU (144.122.0.0/16) and does not respond to recursive queries that come from IP addresses other than METU.  Academic departments and administrative units are advised to use the DNS service run by METU CC instead of running their own DNS servers. 
Link: https://faq.cc.metu.edu.tr/faq/there-domain-name-service-metu

---

## Entry 2521

Question: Is there a FTP Service of METU CC?
Answer: METU FTP archive has a disk capacity of 2 Terrabytes.  The mostly utilized folders are Linux distribtuions (Debian, Fedora/Red Hat, Knoppix, Mandrake, Pardus, Ubuntu), Kernel, virus updates, Firefox, Openoffice etc. METU CC is the official mirror site of      Linux Kernel (http://www.kernel.org/)     Debian OS (http://ftp.debian.org/)     Debian OS Multimedia (https://deb-multimedia.org/)     Debian OS Volatile (http://www.debian.org/volatile)     Pardus OS (http://www.pardus.org.tr/)     Ubuntu OS (http://www.ubuntu.com/)     OpenSUSE OS (http://www.opensuse.org/)  For questions and suggestions you can use [ftpadm@metu.edu.tr]      METU FTP Archive - ftp      METU FTP Archive – http
Link: https://faq.cc.metu.edu.tr/faq/there-ftp-service-metu-cc

---

## Entry 2522

Question: Is there a VOIP Service at METU?
Answer: On the B Class IP block that METU owns, a test environment for voice communication is run without any line out to PSTN telefon circuits. There is an infrastructure up and running for the departments and administrative units that belong to the IP block 144.122.0.0/16.
Link: https://faq.cc.metu.edu.tr/faq/there-voip-service-metu

---

## Entry 2523

Question: What about METU Campus Backbone (METU-NET) statistics?
Answer:   Middle East Technical University's Campus Technical Infrastructure is comprised of a number of departmental networks and various sizes of multi-user hosts connected around a campus-wide backbone network. At the core of campus technical infrastructure, there is this backbone network which is referred as "METU-NET Backbone". METU-NET has been installed in 1990 with 16 connection points, and expanded to 79 connection points in 2009.  The previous Token ring backbone technology is cancelled in 2000 and a new infrastructure based on ATM technology was installed. This backbone was used till 2004 when the new back backbone based on gigabit ethernet technology took its place. Currently, all departments in the campus are connected to the new Gigabit Ethernet Backbone.  Since 2011, METU-NET is supported with 10 Gigabit Ethernet technology.  Each departmental network is comprised of a collection of multi-user and/or single user systems that are connected to a departmental Local Area Network. This departmental LAN is in turn connected to the backbone via ethernet switches with Gigabit uplinks. METU Computer Center (METU CC) has the full responsibility and control over the backbone network (METU-NET). Departments' technical staff operates departmental LANs and METU CC provides technical consultation upon request. You can see the list of department administrative/technical coordinators from this link.  The communication on the campus infrastructure is based technically on Internet Protocol (IP). Both IPv4 and IPv6 are supported.   METU-NET provides its Internet connetion through TUBITAK's (The Scientific and Technological Research Council of Türkiye) ULAKNET (Turkish Academic Network and Information Center). Main Campus' connection to ULAKNET has 10 Gbps capacity. ULAKNET provides a high bandwidth capacity for the main campus and its distant units' (METU Northern Cyprus Campus and Mersin Erdemli Insitute of Marine Sciences) Internet connection.    Mersin Erdemli Institute of Marine Sciences which is not a part of the main campus is connected to METU-NET with a high bandwidth capacity. Likewise, Northern Cyprus Campus is connected to METU-NET with a high bandwith capacity.  Beside this connection,  a spare connection of 1 Gbps capacity is kept ready to be used in case of a problem.  Information about the condition and statistics of off the campus Internet connection can be obtained through http://lines.metu.edu.tr(*)  (*) This links can be accessed only in METU Campus. 
Link: https://faq.cc.metu.edu.tr/faq/what-about-metu-campus-backbone-metu-net-statistics

---

## Entry 2524

Question: What about METU off-campus connection statistics?
Answer:   METU-NET provides its Internet connetion through TUBITAK's (The Scientific and Technological Research Council of Türkiye) ULAKNET (Turkish Academic Network and Information Center). Main Campus' connection to ULAKNET has 4 Gbps capacity. ULAKNET provides a high bandwidth capacity for the main campus and its distant units (METU Northern Cyprus Campus and Mersin Erdemli Insitute of Marine Sciences).    Mersin Erdemli Institute of Marine Sciences which is not a part of the main campus is connected to METU-NET with a high bandwidth capacity. Likewise, Northern Cyprus Campus is connected to METU-NET with a high bandwith capacity.  Beside this connection,  a spare connection of 1 Gbps capacity is kept ready to be used in case of a problem.  You can access the off-campus connection statistics from http://lines.metu.edu.tr (*)  (*) Accessible only from METU IP addresses.  
Link: https://faq.cc.metu.edu.tr/faq/what-about-metu-campus-connection-statistics

---

## Entry 2525

Question: What is webcache?
Answer: 

Important Notice !!!
Library Webcache Service was ended on 5th of August 2014. In order to access the Library Electronic Recources from outside of METU Campus please use the other services which explained in this link below:http://lib.metu.edu.tr/remote-access
What is Web Caching?
Web caching is an efficient method of saving time and easing the burden on the network traffic by keeping  temporary copies of web objects requested by the user (desirable to accessed later to the same remote web sources -such as the data that are accessible via protocols such as HTTP, FTP, Gopher-) on one of the servers of the local area network, where these previously cached objects are instantly returned to the user. so, the average time for returning the requests of users using the same web caching server is reduced and more bandwidth is gained.
 


Link: https://faq.cc.metu.edu.tr/faq/what-webcache

---

## Entry 2526

Question: Why would the CC restrict an IP access?
Answer: 

In accordance with Information Technology Resources Usage memorandum released on 24 March 2004, the CC restricts IP access of a computer connected to the METU campus backbone network when reasons like virus detection etc. are encountered. 
The CC restricts IP access for the reasons mentioned below:
By the requisition of the Unit Computer Coordinator's statement of reason
Upon encountering virus activity
Upon carrying out an unauthorized process
Being observed as a Spam e-mail source
Observing an unauthorized change of IP address
 


Link: https://faq.cc.metu.edu.tr/faq/why-would-cc-restrict-ip-access

---

## Entry 2527

Question: How can I find out my IP address?
Answer: 

You can find out your IP address from http://whatismyip.metu.edu.tr/


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-find-out-my-ip-address

---

## Entry 2528

Question: How can I find out the MAC (physical) address of the Ethernet adapter of my computer?
Answer: 

MAC (Media Access Control) address defines the network interface hardware of a network device or a computer on a computer network. It is a hexadecimal expression that can contain numbers between 0-9 and letters between A-F. Each network interface (Ethernet, wireless, bluetooth etc) has a unique MAC address.
An authentication system based on MAC address runs on the cable network services at the dormitories of METU Campus.
If you are residing in the dormitories you should define the MAC address of the Ethernet adapter of your computer to the system from the address https://netregister.metu.edu.tr in order to make use of the cable network services.

For Windows operating systems;

To open the command prompt window select;
Start > All Programs > Accessories > Command Prompt
or;
Start > Run > cmd
and click OK. Write down the command getmac /v and press Enter. MAC address of your Ethernet card is on the line Local Area Connection on Physical Address column.

Using the command ipconfig /all on command prompt window, you can also find the MAC address of your Ethernet card on the line Physical Address under Ethernet adapter Local Area Connection, as well as some network information such as IP address etc.

 
For MAC OSX operating systems;
Select;
Apple > System Preferences > Network
Choose Ethernet on the list of connection points on the left side and click Advanced.

Select Ethernet tab. MAC address of your Ethernet card is on the line Ethernet ID.

 
For UNIX/Linux operating systems;
 
Network interfaces are labeled such as bge0, ie0, eth0 etc. Sign in as _x0093_root_x0094_, write down the command ifconfig -a on the command line and press Enter. MAC address of your Ethernet card is on the line HWaddr or ether.


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-find-out-mac-physical-address-ethernet-adapter-my-computer

---

## Entry 2529

Question: How can I find out the MAC (physical) address of the wireless adapter of my computer?
Answer: 

MAC (Media Access Control) address defines the network interface hardware of a network device or a computer on a computer network. It is a hexadecimal expression that can contain numbers between 0-9 and letters between A-F. Each network interface (Ethernet, wireless, bluetooth etc) has a unique MAC address.
An authentication system based on MAC address runs on the cable network services at the dormitories of METU Campus. To connect wireless network of METU (meturoam) you can follow https://faq.cc.metu.edu.tr/tr/sss/meturoam guideline.
For Windows operating systems;
To open the command prompt window select;
Start > All Programs > Accessories > Command Prompt
or;
Start > Run > cmd
and click OK. Write down the command getmac /v and press Enter. MAC address of your wireless network adapter is on the line Wireless Network Connection on Physical Address column.

Using the command ipconfig /all on command prompt window, you can also find the MAC address of your wireless network adapter on the line Physical Address under Wireless LAN adapter Wireless Network Connection, as well as some network information such as IP address etc.

 
For MAC OSX operating systems;
Select;
Apple > System Preferences > Network
Choose AirPort on the list of connection points on the left side and click Advanced.

Select AirPort tab. MAC address of your wireless network adapter is on the line AirPort ID.



Link: https://faq.cc.metu.edu.tr/faq/how-can-i-find-out-mac-physical-address-wireless-adapter-my-computer

---

## Entry 2530

Question: How can I find out the MAC (physical) address on a BlackBerry Smartphone?
Answer: 

BlackBerry 4.5 - 5.0 versions:
From the home screen, click Options > Status.
The WLAN MAC field displays the MAC address for the smartphone.   
BlackBerry 6 - 7.1 versions:
From the home screen, select Setup > Options > Device > Device and Status Information.
The WLAN MAC field displays the MAC address for the smartphone.   
BlackBerry 10 OS version:
From the home screen select Settings > Network Connections > Wi-Fi > Advanced.
In the Diagnostic Information drop-down, select  Device Information.
The Physical Address field displays the MAC address for the smartphone.
 
Blackberry Playbook Tablet:
From the Home Screen click on Options.
Next select About.
Next Select Network from drop down menu.
 

Link: https://faq.cc.metu.edu.tr/faq/how-can-i-find-out-mac-physical-address-blackberry-smartphone

---

## Entry 2531

Question: How can I find out the MAC (physical) address on a Nintendo DS?
Answer: 

To locate the MAC Address of your Nintendo DS, you will need a WiFi-enabled game for the Nintendo DS, then follow these steps:
Go to the Nintendo WiFi Connection Setup in the game's menu.
Select Options and System Information.
The MAC Address is displayed on the top line.
 

Link: https://faq.cc.metu.edu.tr/faq/how-can-i-find-out-mac-physical-address-nintendo-ds

---

## Entry 2532

Question: How can I find out the MAC (physical) address on a Nintendo Wii?
Answer: 

From the Wii Channel menu, select "Wii Settings" (the round button on the bottom-left of the screen with "Wii" on it).
Select "Internet"
 then "Console Settings."
The MAC address of the Wii console is displayed on the first line.
 


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-find-out-mac-physical-address-nintendo-wii

---

## Entry 2533

Question: How can I find out the MAC (physical) address on a Nokia E5/E7?
Answer: 


1. Navigate to the Home screen.

2. On the keypad, enter in *#62209526#. 
 


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-find-out-mac-physical-address-nokia-e5e7

---

## Entry 2534

Question: How can I find out the MAC (physical) address on a Samsung Smartphone?
Answer: 

To locate the MAC Address of your WiFi-enabled Samsung smartphone, follow these steps:
From the main screen, select Menu.
Select Settings.
Select WiFi.  
Select Available networks.
Select Options.
Select View Details. 
Scroll to MAC Address.
Note: These steps may differ depending on the device you have. For more specific instructions, please refer to the documentation that came with your smartphone.
 


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-find-out-mac-physical-address-samsung-smartphone

---

## Entry 2535

Question: How can I find out the MAC (physical) address on a Windows Mobile Device?
Answer: 

To locate the MAC Address of your Windows Mobile device, follow these steps:
On Start, click left to the App list.  
Tap Settings, then About, then More info.   
Note the MAC Address.
 

Link: https://faq.cc.metu.edu.tr/faq/how-can-i-find-out-mac-physical-address-windows-mobile-device

---

## Entry 2536

Question: How can I find out the MAC (physical) address on an Android Smartphone?
Answer: 





 1. Under your Applications, select Settings.  2. At the very bottom of the list, choose "About Device (Android Phones may say About Phone).  3. Choose Hardware Information. 4. Your MAC Address will be listed under Wi-Fi MAC Address. MAC






Link: https://faq.cc.metu.edu.tr/faq/how-can-i-find-out-mac-physical-address-android-smartphone

---

## Entry 2537

Question: My IP access has been restricted. How can I find out the reason?
Answer: 

You can find out why your access has been restricted from https://netregister.metu.edu.tr -> Restriction menu.


Link: https://faq.cc.metu.edu.tr/faq/my-ip-access-has-been-restricted-how-can-i-find-out-reason

---

## Entry 2538

Question: What should I do to reactivate the IP access of my computer?
Answer: 

If your computer's IP access has been restricted, you should first remove the cause of the problem which can be found on the list at www.netregister.metu.edu.tr -> Restiriction.
In order to remove the network restriction on which IP-MAC matching is in use, such as dormitories, some departments and METU wireless network, sign in to www.netregister.metu.edu.tr with your user name and password.      If the IP access of a device which is registered to your use account is restricted, click  Restriction(s) which is displayed on the screen.       You can see the restricted MAC address on the next screen. Click Details to see the details.      If you solve the problem that caused restriction click Remove Restriction to reactivate the MAC address. You can only do this once on the same day.      If you cannot see the Remove Restriction button, there may be a serious situation that you must talk to METU-CC. In this case open a support ticket via https://itsupport.metu.edu.tr/ including your MAC address.
Then you will receive a message that your IP restriction has been removed.   


Link: https://faq.cc.metu.edu.tr/faq/what-should-i-do-reactivate-ip-access-my-computer

---

## Entry 2539

Question: How can I connect to eduroam wireless network using my Mac computer?
Answer: 

You can connect to eduroam by downloading and executing the configuration file to your iOS device.
Download configuration file for iOS devices.
on User Account option, user_namemetu.edu.tr and password should be entered.
 
Please follow the steps below if you would like to create the configuration file by using your MAC OSX device.
 To connect to the eduroam network, please install Apple Configurator from AppStore.

Run the application and click Start Preparing Devices.

 
 
Activate Supervision. (Turn ON)
 

 
 

Click + at the bottom of the window and select Create New Profile in the menu.
 

 
 
In the popup window, click Wifi and then configure.
 

 
 
Type eduroam and select WPA/WPA2 Enterprise in the Security Type combo box.

 
 
Select TTLS under Accepted EAP types heading.
 

 
 
Type your METU user name and password. Then, select PAP in the Inner Authentication heading and click Save to save the profile.
 

 
Click on the profile name and export it to your computer by clicking the + at the bottom of the window.

 
 
 
 

 
Locate the exported profile and install it to your computer double clicking it.
 
 

 

 

 
 

 
 


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-connect-eduroam-wireless-network-using-my-mac-computer

---

## Entry 2540

Question: How can I connect to eduroam wireless network via an Android operating system installed phone?
Answer: 

In order to connect eduroam wireless network, select Settings > Wireless and network > Wi-Fi settings.

 

Tap "eduroam" on the network list. Choose TTLS from "EAP method" list and PAP from "Phase 2 authentication" list. Leave "CA certificate" and "User certificate" as Unspecified. Write down your e-mail address on "Identity" field and your password on "Password" field. Leave "Anonymous identity" field blank and tap Connect. Please visit Advanced / Gelişmiş menu for Phase 2 authentication options in new Android phones.

 

After these steps you can see the icon on the top status bar notifying that you are connected.
on User Account option, user_namemetu.edu.tr (example: e123456) and password should be entered.
on newer devices, there is an option called "domain name" and you need to enter "border.metu.edu.tr" "netlogin.metu.edu.tr" to that field.
!!! Wireless network connection problems are observed in some of Android devices using Android 6 and prior versions. Occasionally these devices display there is an established wireless connection on the screen but when you try to connect to the Internet, they fail. This problem is originated from a bug in the operating system. The bug cause Android devices to continue to use DHCP-leased IP addresses after the leases expire, and cause Android devices to resume using IP addresses from expired DHCP leases. When you face the the same problem please disable your Wi-Fi connection and enable it again.


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-connect-eduroam-wireless-network-android-operating-system-installed-phone

---

## Entry 2541

Question: How can I connect to eduroam wireless network via my iPhone?
Answer: 

You can connect to eduroam by downloading and executing the configuration file to your iOS device.
Download configuration file for iOS devices via Safari webbrowser. Then please install downloaded config file (metu_eduroam.mobileconfig) from setting screen of Iphone device (settings-general-profile).  After installation has been completed, select the eduroam wireless network to connect.
On User Account option screen, user_namemetu.edu.tr and password should be entered.
 


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-connect-eduroam-wireless-network-my-iphone

---

## Entry 2542

Question: Does eduroam work in different environments?
Answer: 

eduroam can work with operations systems and devices like Windows XP, Windows Vista, Windows 7, Windows 10, Linux, Windows CE, iphone, ipod, etc.


Link: https://faq.cc.metu.edu.tr/faq/does-eduroam-work-different-environments

---

## Entry 2543

Question: How to connect to eduroam?
Answer: 




What do you have to do if you want to connect to eduroam?
Microsoft Operating Systems
Linux Based Operating Systems  
Mac OS
IPhone 
Android Operating Systems
Certificates
Microsoft Windows
The users who use Microsoft Windows operating systems (Windows 7 and previous versions) has to use the SecureW2 program to be able to make IEEE 802.1x and EAP configurations. For this reason SecureW2 : The free 802.1x/EAP client for Windows(32 bit) should be installed on the computer. This client works only on the 32 bit Windows operating systems (Windows XP, Vista, 7). For SecureW2 to be active, the manager for wireless networks must be chosen to be Windows, and all other third party software has to be disabled.
For Windows 8 and later versions of Microsoft Windows operating systems (including 32 and 64 bit), there is no need for any software installation.
Below examples are given on explanations regarding how to connect to METU network form different platforms. To connect your own institutions network, please contact you network administrator.


Microsoft Windows VISTA ve 7 ayarları
Click for descriptions with pictures. 
Click START menu on the operating system, and open the windows respectively:
START > Control Panel > Network and Sharing Center > (from the menu on the left) Manage Wireless Networks
Here, tright click on the eduroam ssid (service set identifier) and choose Properties, on the windoweduroam Wireless Network Properties window that's opened, changes on the Security heading should be done:
Security type: WPA2 Enterprise
Encryption Type: AES
Choose a network authentication method : SecureW2 TTLS should ve choosen.
Beside Secure W2 TTLSoption, on SecureW2 menu when clicked on Settings:
Profile: click Configure under DEFAULT 
on Connection option,  Use alternate outer identity and Use anonymous outer identity should be choosen.
on Certificates option Verify Server Certificates option should ve removed.
on Authentication option PAP should ve choosen.
on User Account option, user_namemetu.edu.tr and password should be entered.

Microsoft Windows 10 Configuration
In the wireless connections list, please connect to eduroam and provide your METU usercode (with @metu.edu.tr) and METU password. After you authenticate the certificate, you are connected to eduroam network.
IMPORTANT: If you upgraded from previous versions of Windows 10, you need to uninstall any connection utilities like SecureW2, click "forget eduroam" and reconnect it with the above instructions.
 
Linux Operating Systems:
Description with pictures for Ubuntu distribution
In Linux operating systems, the the help of the wpa_supplicant, it's possible to connect to 802.1x wireless networks running on WPA or above. So to connect to eduroam, the wpa_supplicant application should be installed beforehand.
This operation can be held with the apt-get install wpasupplicant command in debian based operating systems. In other Linux distributions, you can use you package manager to make the installation.
Linux Configuration
To the folder /etc/wpa_supplicant or to where the installation took place, generate a file named wpa_supplicant.conf and configure the file as follows (use your own username and password)
network={
 ssid="eduroam" key_mgmt=WPA-EAP pairwise=AES group=AES eap=TTLS phase2="auth=PAP" anonymous_identity="anonymousmetu.edu.tr" identity="user_namemetu.edu.tr" password="your_password"
} 
Connect to the wireless network by entering the command edited according to your network adapter:
wpa_supplicant -B -i eth2 -c /etc/wpa_supplicant/wpa_supplicant.conf -D wext (for use of wpa_supplicant refer to man wpa_supplicant and man wpa_supplicant.conf commands)
To get the ip address automatically, enter the command dhclient eth2 
For the configuration to automatically, in /etc/network/interfaces file, the line regarding the adapter should be changed with this one. (eth2 in the example)
 auto eth2 iface eth2 inet dhcp wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
Certificates
The links of the certicates that are needed to connect the wireless network are as follows:
certificate in .der format
certificate in .pem format





Link: https://faq.cc.metu.edu.tr/faq/how-connect-eduroam

---

## Entry 2544

Question: I forgot eduroam password, what can I do?
Answer: 

To connect to the eduroam network, you need to use your METU usercode and password. If you cannot remember your password, please visit http://faq.cc.metu.edu.tr/faq/i-forgot-my-password-where-can-i-apply


Link: https://faq.cc.metu.edu.tr/faq/i-forgot-eduroam-password-what-can-i-do

---

## Entry 2545

Question: I frequently disconnect/can not connect to the eduroam network?
Answer: 

To use the eduroam network in a healthy way, the devices drivers of your computer's wireless network adapter should be up to date. Get help from the technical support group of your adapter's vendor.


Link: https://faq.cc.metu.edu.tr/faq/i-frequently-disconnectcan-not-connect-eduroam-network

---

## Entry 2546

Question: What is eduroam? 
Answer: 


METU eduroam wireless network, that was initiated by METU CC in October 2007, has been the first among Turkish universities to take part in the eduroam project (eduroam is an abbreviation for educational roaming)
eduroam, working on RADIUS-based 802.1x security standard, aims seamless network usage of users of eduroam member institutions in other member educational institutions. The user of an eduroam member institution can use his/her username and password duo to connect to another member institution's eduroam wireless network. The user sends a request to the host institution, while the host institution's authentication server directs the connection request to the home institution's authentication server and the user is determined whether or not  to be authorized by the home authentication server. All these queries are sent back and forth between servers through an encrypted tunnel, hence the user name and password pair is visible only in the home server. The only thing user needs to do in this case, is to define the visitied institution eduroam wireless network like their institution's network.



Link: https://faq.cc.metu.edu.tr/faq/what-eduroam

---

## Entry 2547

Question: What is security level of eduroam?
Answer: 

Today, the well known security technologies in wireless neotworking are WEP, WPA, WPA2. The security level of WEP and WPA are today very low level. For that reason our setup files come predefined with WPA2. But WPA-TKIP is temporarily in use.


Link: https://faq.cc.metu.edu.tr/faq/what-security-level-eduroam

---

## Entry 2548

Question: What is the technical structure of eduroam?
Answer: 

In METU campus three (3) different brands of wireless access points are  used. These are Aruba, Cisco and HP Procurve.
  


As can be understood from the drawing, the infrasturcture in METU uses WPA2 security standard. Besides this security solution, TTLS (PAP) is used to autenticate users in an easy way. In this structure the user needs only a certificate for EAPP, user certicicate is not used. The requent coming to the RADIUS server constitutes a mutual tunnel and the information that comes through this tunnel is analyzed by RADIUS and queried to LDAP over the secure network. If LDAP authenticates the user's username and password, the system accepts the user.




Link: https://faq.cc.metu.edu.tr/faq/what-technical-structure-eduroam

---

## Entry 2549

Question: Who are the Türkiye eduroam members? 
Answer: 


eduroam member institutions
 You can access the up to date list of Turkish participant institutions through eduroam Türkiye's web site.



Link: https://faq.cc.metu.edu.tr/faq/who-are-turkiye-eduroam-members

---

## Entry 2550

Question: Why do I have to install a program for connecting eduroam?
Answer: 

The most important issue in eduroam is the security issue. In classical wireless networks, it's possible that someone can listen to the communication data. The only way to prevent this is to increase the complexity of the encryption method. Starting from the first moment you send your username and password, the communication is provided with encryption. Since the program for starting this TTLS algorithm is not present in Windows operation systems, we have to use a different program.
If you are running Windows 10, this algorithm is builtin and you do not need to install a program.


Link: https://faq.cc.metu.edu.tr/faq/why-do-i-have-install-program-connecting-eduroam

---

## Entry 2551

Question: How can I reach to department coordinator?
Answer: 

You can reach to department coordinators list via http://coordinators.metu.edu.tr/


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-reach-department-coordinator

---

## Entry 2552

Question: What should I do to reactivate the IP access of a computer that I am responsible of as a coordinator?
Answer: 

If an IP access of a computer that is related to you as a department computer coordinator has been restricted, you should follow the steps below:
In order to remove the restriction, sign in www.netregister.metu.edu.tr with your METU username and password.
   If an IP address that you are responsible for was restricted, you would see the Restriction menu after you login. This menu does not appear if there is no IP restriction. Click the Restriction menu to see the restrictions.
   You can see the list of restricted IP and MAC addresses on the next screen. Click Details to see the details.
   If you solve the problem that caused restriction click Remove to reactivate the MAC address.
   If you cannot see the Remove Restriction button, there may be a serious situation that you must talk to METU-CC. In this case open a support ticket via https://itsupport.metu.edu.tr/ including IP and MAC address of the restricted device.
After you click the Remove Restriction button, you will receive a message that your IP restriction has been removed. In some cases you might need to disconnect the device, wait for 5 minutes, and then connect it again.



Link: https://faq.cc.metu.edu.tr/faq/what-should-i-do-reactivate-ip-access-computer-i-am-responsible-coordinator

---

## Entry 2553

Question: How can I connect to INTERNET from dormitories?
Answer: 

For the users who stay in the dormitories and want to use the local cable network, the first step is that the dormitory manager registers the user in the dormitory automation system.
This process is conducted by the manager of the dormitories for each student during the registration to the dormitories. After the dormitory manager completes the registration, users have to sign in with their central system user name and password at https://netregister.metu.edu.tr
Users can obtain access to the cable network after entering their MAC address information in Wired Network menu in netregister.metu.edu.tr
Users stay in the summer time dormitories should be sure about their dormitory registration made for right dormitory. To do this, they can consult their dormitory manager or Directorate of Dormitories (2nd dormitory building) to get information. If users are not registered to any dormitory or their registration was made to wrong dormitory, they won't be able to make their own wired network registration on the netregister interface (https://netregister.metu.edu.tr/).
Note: Since DHCP is used (i.e. recognized automatically) in all dormitories, the users in the dormitories can connect to the internet after completing all the steps defined above. They do not have to enter TCP/IP settings. Moreover, users who stay in those dormitories can also reach https://netregister.metu.edu.tr through local cable network before registration in order to complete their registration.
Steps, in order to be connected to the internet after obtaining IP address information, are as follows:
Be sure that your computer recognizes your Ethernet card. You can find it by clicking right to the computer icon, choosing properties, then device manager and network card. If your computer recognizes Ethernet card, that is, the right software is installed, you can continue without any problem. If there is an exclamation mark on the device icon, that means your computer does not recognize the Ethernet card. Then, you have to install the right software.
Next step is the configuration of TCP/IP settings. Click right on the computer icon on the desktop, choose properties, then TCP/IP settings, and then choose properties. You can complete the settings by selecting "Obtain automatically"  in the relevant boxes and then clicking OK. Almost in all Windows operating systems, the configuration of TCP/IP settings is conducted similarly.
Lastly, in order to connect to the cable network, it is necessary to obtain a UTP network cable from electronic stores.  You should measure the distance between the location of your computer and network plug. After connecting the UTP network cable to your computer and plug, you should be able to connect to METU cable network.
It is suggested for the users who utilize network connection in the dormitory regions to read the Dormitory Rooms Computer Network Rules.





You can visit https://faq.cc.metu.edu.tr/faq/how-can-i-find-out-about-source-my-network-connection-failure-dormitories if you have any problems connecting to the cable network. You can also send an IT support request via https://itsupport.metu.edu.tr







Link: https://faq.cc.metu.edu.tr/faq/how-can-i-connect-internet-dormitories

---

## Entry 2554

Question: How can I find out about the source of my network connection failure at the Dormitories?
Answer: 

Please review the following if you have problems with your wired network connection problem at the dormitories.
1. To solve your connection problem, read the following conditions first.
1.1. In case of violations of the rules regarding internet usage, the internet access of the students may be blocked automatically. In such cases, you will be informed via e-mail. Please check your METU e-mail. You can also get information from the "Restrictions" section when you log in to https://netregister.metu.edu.tr.
1.2. Log in to https://netregister.metu.edu.tr/  using your own user information. Check if the physical address (MAC address) of your device with the internet connection problem is registered in the system. If it is not registered, find out the physical address of your device and register it in the system. The following links are useful if you don't know how to get your device's MAC address.
http://faq.cc.metu.edu.tr/faq/how-can-i-find-out-mac-physical-address-ethernet-adapter-my-computer
https://faq.cc.metu.edu.tr/faq/how-can-i-find-out-mac-physical-address-ethernet-adapter-my-computer
1.3. The internet connection provided by Middle East Technical University should be used within the framework of METU Information Technology Resources Use Policy (See https://www.metu.edu.tr/it-use-policy) Any actions that are contrary to this policy may prevent the students from accessing the internet or penalty sanctions. Internet sharing through hotspots or other software is one of the most common rules violations and may be another reason for blocking students' connections.
1.4. Try connecting your device to the internet with another internet patch cable or another wall outlet that you know as working properly.
If you can connect with a different internet patch cable in your own wall outlet, your cable is defective, you need to renew your cable.
If you can connect with your own cable at a different outlet, please inform the Dormitory Reception to have your own network checked.
1.5. Make sure that your device is free from viruses or malware. Scan your device for viruses in any case. If your device still contains virus software, you can try restoring the system. Please visit the following links for more information:
https://support.microsoft.com/tr-tr/help/17127/windows-back-up-restore for Windows PCs
https://support.apple.com/tr-tr/HT201250 for MACs
2. If you are using the USB or Thunderbolt port to connect your computer to the Internet, make sure your Ethernet to USB or Ethernet to Thunderbolt converter is connected and working properly. If an authorized driver is provided for the use of such converters, make sure that the driver is installed and up to date. Also, check that the MAC address registered in the system is the same as the MAC address of the Ethernet converter you are using. If your device has an Ethernet port, check that your Ethernet card is plugged in and enabled, and if so, the driver is installed and up to date. 
3. It is recommended that you do not use any types of equipment between your computer and the wall outlet.
If you could not resolve the connection problems, please visit us at Computer Center room B-14 with your computer. Remember to bring any Ethernet converters you use, if any.


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-find-out-about-source-my-network-connection-failure-dormitories

---

## Entry 2555

Question: What are the Dormitory Rooms Network Rules and Regulations of Use?
Answer: 1. The use of network resources (network connection, user codes, IP-MAC address combination, campus /off-campus access etc.), which are allocated for the personal computers of the students in the dormitories, is subject to the rules and conditions set forth within "METU Computing and Networking Ethics" which is available at this address: https://www.metu.edu.tr/it-use-policy
2. The state allocates and grants to the University financial resources in order to accomplish computer networking technology investments that will primarily aid the instructional, academic, research and administrative objectives of the University. The personal use of the network facilities by the users should in no way disrupt access priorities of those users that use the network for such instructional, academic, research and administrative objectives. In this respect, the users can find the guidelines for the appropriate use of network resources, the rules and regulations that the users must comply with and misconducts & prohibited behaviours as below:
 KaZaA, iMesh, eDonkey2000, Gnutella, Napster, Aimster, Madster, FastTrack, Audiogalaxy, MFTP, eMule, Overnet, NeoModus, Direct Connect, Acquisition, BearShare, Gnucleus , GTK-Gnutella, LimeWire, Mactella, Morpheus, Phex, Qtella, Shareaza, XoLoX, OpenNap, WinMX, DC++, BitTorrent etc..
a. Peer-to-peer (P2P) file sharing programs, as well as violating copyright and licensing rules, use up an excessive amount of bandwidth that consequently hinders the use of network resources for purposes of priority. For this reason, it isstrictly forbidden to use the "peer-to-peer" file sharing programs. Such usage includes, but is not limited to, the following programs:
b. It is expressly forbidden to use wireless network resources for commercial purposes or for activities of private gain.
c. It is forbidden to use network resources for mass mailing, mail bombing, sending spam and users are not allowed to provide the means to the third parties to perform similar acts.
d. It is prohibited to keep possession of server computers in the dormitory that provide internet service (web hosting service, e-mail service etc.)
e. Users must not intentionally allow others to use University network resources from outside or, in other words, users must not pave the way for others to exploit privileges and act as if they are authorized to own the legitimate rights of the University users. (proxy, relay, IP sharer, NAT etc.)
f. It is forbidden to commit activities that threaten the security of the network (DoS attack, port-network scan etc.)
g. A unique IP number is assigned to each and every computer. Users are not permitted to change this IP number and/or the MAC (Media Access Control) address. IP settings of the computer should be configured according to the settings in the network device registration website (netregister.metu.edu.tr).
h. Networking facilities in the dormitories (network connection, user codes, IP-MAC address combination, local/off-campus access etc.), which are granted as a privilege to the students, will be used by every student in an appropriate, legal, ethical and considerate manner in accordance with the codes of behaviour and the regulations. It is the sole responsibility of all students that they are not endangering the safety of the resources by providing intentionally or unintentionally the means to the third parties to access to network resources. The student alone is answerable and accountable for every unwanted and unlawful consequences that may result from this act.
3. If the use of the computing and networking facilities is proven to be incompatible with the educational and scholarly missions of the University, and if the user has been proven to behave irresponsibly, inappropriately, unethically and illegally; in a manner displaying disruptive and inappropriate conduct that endanger the efficiency, integrity, safety and continuity of networking services; and if the user breaches the rules and regulations set forth in this document, one or more of the following disciplinary actionsmay be taken as a reasonable response to eliminate and remedy the threatening and abusive behaviour;
local and/or off-campus network access privileges may be restricted,
local and/or off-campus network access privileges may be suspended, modified or witheld,
the user codes and user accounts on the central server systems may be terminated,
the disciplinary mechanisms such as investigation or prosecution may be initiated,
judicial proceedings may be started.
4. The student, who has been proven to have disregarded or violated the rules and regulations, will be forewarnedby the Directorate of Dormitory.
5. These rules and regulations become effective as soon as they are publicized. The University and Computer Center reserves the right to amend these Rules and Regulations at any time without prior notice. The updated version of the rules and regulations can be viewed in the following address:
6. For your questions and problems, you can reach us via "Contact Us" link on METU Computer Center website or https://itsupport.metu.edu.tr/
Please click here: https://faq.cc.metu.edu.tr/system/files/u2/dorm_guestusers.pdf  to download the form.


Link: https://faq.cc.metu.edu.tr/faq/what-are-dormitory-rooms-network-rules-and-regulations-use

---

## Entry 2556

Question: How can I learn whether my ip address has restricted or not?
Answer: 

The access of IPs may be resitricted beacuse of the SPAM, Viruses, unauthorized usage, P2P Sharing, and breach of license for a limited time or indefinite by the METU-CC. You can check the status of your IP by the link below: 
https://netregister.metu.edu.tr -> Restriction Menu
The users has the restricted IPs, after solving the problem caused to the restriction may login https://netregister.metu.edu.tr with their METU username and password and remove the restriction.
Some restrictions may not appear on the Restriction menu, or the you may not be allowed to remove the restriction by yourself. In such a case, please reach us via "Contact Us" link on METU Computer Center web site with your restricted MAC address. Your status will be examined and returned to you as soon as possible.
 


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-learn-whether-my-ip-address-has-restricted-or-not

---

## Entry 2557

Question: How to connect Wired Network?
Answer: To access wired network from dormitories click here: https://faq.cc.metu.edu.tr/faq/how-can-i-connect-internet-dormitories-turkish
To access wired network from residences click here: https://faq.cc.metu.edu.tr/faq/how-can-i-connect-internet-residences-turkish
To access wired network from the other department/units is needed to communicate with Network Managers of the related departments.
Link: https://faq.cc.metu.edu.tr/faq/how-connect-wired-network

---

## Entry 2558

Question: My Internet connection is very slow. What is the problem?
Answer: 

Our users are sharing the common Internet bandwidth of campus network. Connection speed of every user decreases as much as the number of the users sharing the network increases.
Therefore, as the number of complaints reported from our users increase, "Shaping Excessive Usage" policy started to be executed. In this context, Internet speed of the users who affect others_x0092_ network usage will be shaped due to the procedures and sanctions of the 5th article of METU Information Technology Resources Use Policy. This procedure will be valid only towards the off-campus traffic, i.e. all addresses but *.metu.edu.tr in general. There is no such limitation for within-campus connections.
First of all, please try connecting to the network with a different network patch cable. If this works, then your previous network patch cable is probably broken. Obtain a new network patch cable.Please try connecting to the network from another network outlet. If this works, then there might be a problem with your original network outlet. In the dormitories, you can inform the reception desk and have your network outlet controlled.
If these procedures didn't resolve your problem, please visit https://faq.cc.metu.edu.tr/faq/how-can-i-find-out-about-source-my-networ....
In addition, in case of low internet speed, you can also check below statements;- Low quailty of cable you use between your computer and the data socket on the wall (cable damage, use of unstandardized cable), use of high quailty and undeformed internet cable will solve the issue.- Use of internet cable with damaged connector.- Use of internet cable with damaged external protection.- Folding of internet cable with sharp angles. - Tying of internet cable- Use of wrong modeled and outdated ethernet card driver- The computer’s wired network port is not clean (dust and liquids cause to have problem)- The computer’s wired network port is deformed (it can damaged or oxidize over time)- Having applications running in the background that may affect internet traffic (should be examined and unnecessary ones should be closed)- Having applications (Botnet etc.) that make download/upload operations in the background without the user’s knowledge (security scans should be done and the computer should be kept up to date).- High rate of instant user density (high number of users will slow down the speed)


Link: https://faq.cc.metu.edu.tr/faq/my-internet-connection-very-slow-what-problem

---

## Entry 2559

Question: METU VPN Service Use Policy
Answer: 

 METU VPN Service Use Policy
Aim of METU VPN Service
The aim of the METU VPN service is, to enable our staff and students to access the network services which are only permitted to METU campus IP block (144.122.0.0/16), even if they are out of the campus.
 Rules for Using METU VPN Service
1. The METU VPN Service, which is provided to METU staff and students, should be used in accordance with the METU Information Technology Resources Use Policy which is given on the link
2. The state allocates and grants to the University financial resources in order to accomplish computer networking technology investments that will primarily aid the instructional, academic, research and administrative objectives of the University. The personal use of the VPN service by the users should in no way disrupt access priorities of those users that use the network for such instructional, academic, research and administrative objectives.
3. In this respect, the users can find the guidelines for the appropriate use of VPN service; the rules and regulations that the users must comply with and misconducts & prohibited behaviors as follows
3.1. Using Peer-to-peer (P2P) file sharing programs via VPN connection, is strictly forbidden. VPN users should disable such applications before connecting to VPN service and keep them off during their VPN usage.
3.2. It is forbidden to use VPN service for commercial purposes or for activities of private gain.
3.3. It is forbidden to use network resources for mass mailing, mail bombing, sending spam and users are not allowed to provide the means to the third parties to perform similar acts.
3.4. It is forbidden to make any activity that my risk the security of other users, such as DOS or port scan.
3.5. VPN users are responsible for any damage arising from the use of METU VPN service as well as, intentionally or non-intentionally allowing others to use this service.
4. Users who are found to violate these rules, can be applied one or more of the below penalties.
4.1. Restraining the use of VPN service,
4.2. Disabling the user code on the central systems or changing the password,
4.3. Starting investigation via University Authorities,
4.4. Starting legal investigation.
5. The student, who has been proven to have disregarded or violated the rules and regulations, will be forewarned via on-line written notice. Any user who has failed to receive the notice, can get information from METU IT Support Team (https://itsupport.metu.edu.tr/)
6. These rules and regulations become effective as soon as they are publicized. The University and Computer Center reserves the right to amend these Rules and Regulations at any time without prior notice. The updated version of the rules and regulations can be viewed in the same address. You can contact hotlinemetu.edu.tr for your questions.
 
SERVICE CONDITIONS
1. All METU students and staff can use VPN service in accordance with METU Information Technology Resources Use Policy.
2. METU VPN service will be operational 7x24 except outages.
3. In case of failure;
3.1. The service failures, occurring within working hours will be fixed as soon as possible.
3.2. The service failures, occurring outside working hours will not be treated as urgent and will be fixed starting from next business day.
3.3. In case of hardware failure it is possible have long outages.
4. Long outages of VPN service will announced on METU web page.
5. VPN service will be provided with a maximum of 8 Mbps for each user.
6. Opened VPN sessions will end automatically after 24 hours. Users who want to use the service longer, should re-login within 24 hours.
 
LEGAL DISCLAIMER
1. All the risks arising from use of VPN service, are under responsibility of the user. METU Computer Center is not responsible for any risk or damage caused by the use of the service.
2. METU Computer Center is not responsible for any risk or damage caused by the interruption of VPN connection or outage of the service.
3. METU Computer Center restricts access to some network services and web pages via VPN without notice.
                                                                                                                                                                                                                                                                                                                                                                                                Last Updated: 28/03/2016 - 16:30


Link: https://faq.cc.metu.edu.tr/faq/metu-vpn-service-use-policy

---

## Entry 2560

Question: What is VPN Service?
Answer: 

With METU VPN Service, by installing a packaged program (VPN Client) on personal computers and/or mobile devices, our members and students could access to our campus network resources when they are outside the campus.
To use VPN Service on your device follow the steps in faq.cc.metu.edu.tr related with your devices' operating system.


Link: https://faq.cc.metu.edu.tr/faq/what-vpn-service

---

## Entry 2561

Question:  I have problems installing VPN services, what can I do?
Answer: 

If you have installed Aruba VIA application but experience problems connecting to VPN service, please visit https://faq.cc.metu.edu.tr/faq/i-have-problems-vpn-services-what-can-i-do
If you have errors while installing Aruba VIA in Windows:
During our trials, in Windows 10 64 bit running Symantec Endpoint protection, even if the real-time protection is disabled, the VPN application and setup failed. With both Symantec and Aruba VPN uninstalled and then only Aruba VPN installed, VPN connection can be established)
If you have "Virtual Intranet Acccess (VIA) setup wizard ended prematurely" error message, please follow the following steps, especially deleting devices from the Device Manager:
make sure that there are no devices with names VIA or Aruba under Device Manager / Network adapters. If there are any, delete them.
If there are any unknown devices under Device Manager / Network adapters, delete those devices, as well.
check for Windows updates
some software on your computer may be blocking the installer. Please make sure that there is no antivirus software on your computer (Symantec, Mcafee, Avast, etc.) 
start Windows in safe mode and then restart it in normal mode (https://support.microsoft.com/en-us/windows/start-your-pc-in-safe-mode-i...)
check the name of your PC. If there are any Turkish (or non-latin) characters, rename your PC. (https://support.microsoft.com/en-us/windows/rename-your-windows-10-pc-75...)
reboot your PC
try installing again

If you still have problems installing the software, please run the installer from an administrative command prompt as Aruba-VIA-4.5.0.0.2301057-64/l*v log.txt (replace Aruba-VIA-4.5.0.0.2301057-64.msi with the name of the installer file you have) and send us the log file along with the output of winver command.
If you have problems installing in Ubuntu 20.04:
Follow the following steps:
1. Download the installer from here.
2. Run the following from a command prompt, as root
# dpkg -i <file name>
(e.g. "dpkg -i via_4.0.0-2004190.Ubuntu16.04_amd64.deb"  )



Link: https://faq.cc.metu.edu.tr/faq/i-have-problems-installing-vpn-services-what-can-i-do

---

## Entry 2562

Question: Can I use different VPN softwares to use METU VPN Service?
Answer: 

 You have to use Aruba Via software which published at https://netregister.metu.edu.tr to use METU VPN service. You can't use METU VPN service with using VPN software which embedded to operating systems or using other third party VPN softwares.


Link: https://faq.cc.metu.edu.tr/faq/can-i-use-different-vpn-softwares-use-metu-vpn-service

---

## Entry 2563

Question: How can i use METU VPN Service on MAC OS X installed devices?
Answer: 

With METU VPN Service, by installing a packaged program (VPN Client) on personal computers and/or mobile devices, our members and students could access to our campus network resources when they are outside the campus.
Warning: For users using VPN, the connection speed per user is defined as 8 Mbps. For this reason, in the cases that VPN connection is not necessary it is recommended that you disconnect from your VPN connection.
To use VPN Service on your MAC OS X installed device follow these steps:
Login to netregister.metu.edu.tr
Click VPN service and download the installation file for your Operating System. For MacOS Mojave and Catalina, please go to App Store and install the latest Aruba Via software.
Run the installer and Click Next, Install buttons where applicable. During setup, somehow you may not be able to click Continue button since it is grayed out. In order to select you need to change some security settings of your operating system. From your System Preferences, click Security & Privacy and then in the section "Allow applications downloaded from", click Anywhere. If it is not selectable, you may click lock icon at the bottom of the window and enter your administrator password. You can continue the setup process afterwards.
When the installation has finished, enter border.metu.edu.tr as Remote Server and your METU username and password into the fields as your connection credientials. Click Login. Select default profile.

Service will open as Not Connected. If you want to Connect you can initiate a VPN connection by clicking Connect button on Connection Details tab. 
Warning: The connection speed per user is defined as 8 Mbps. For this reason, in the cases that VPN connection is not necessary it is recommended for you to disconnect from VPN.
If the VPN Client installer file, which you downloaded to your MAC, is opened with Text Editor program instead of starting installation of program. it is most probably because the file is downloaded with wrong or no file extension. Change the file extension with .dmg for the program works correctly.


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-use-metu-vpn-service-mac-os-x-installed-devices

---

## Entry 2564

Question: How can i use METU VPN Service on my Android device?
Answer: 

With METU VPN Service, by installing a packaged program (VPN Client) on personal computers and/or mobile devices, our members and students could access to our campus network resources when they are outside the campus.
Warning: For users using VPN, the connection speed per user is defined as 8 Mbps. For this reason, in the cases that VPN connection is not necessary it is recommended that you disconnect from your VPN connection.
To use VPN Service on your Android device follow these steps:
 
 Touch "Play Store".
 

Enter "Aruba Via" in the search box.
 

 Touch "Install".
 



 Touch "Accept".
 



 Touch "Open".
 

 Touch "Aruba Via".
 

 Enter "border.metu.edu.tr" on log in screen. Enter your “METU user code” and “password”. Touch Login.
 
Select default profile.

 Open "VPN" connection by sliding to the right.
 



 "VPN" connection is ready.



 


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-use-metu-vpn-service-my-android-device

---

## Entry 2565

Question: How can i use METU VPN Service on my iPhone or Ipad?
Answer: 




 Touch "App Store".
 

 Enter "Aruba Via" in the search box. Touch "Free".
 



  Touch "Install".
 

 Enter "Password". Touch "OK".
 



 Touch "Open".
 



 Enter "border.metu.edu.tr" on log in screen. Enter your METU user code and password. Touch Login.

 select default profile.

 


Open "VPN" connection by sliding to the right.
 



 "VPN" connection is ready.


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-use-metu-vpn-service-my-iphone-or-ipad

---

## Entry 2566

Question: How can i use METU VPN Service on Ubuntu OS installed devices?
Answer: 


With METU VPN Service, by installing a packaged program (VPN Client) on personal computers and/or mobile devices, our members and students could access to our campus network resources when they are outside the campus.

Warning: For users using VPN, the connection speed per user is defined as 8 Mbps. For this reason, in the cases that VPN connection is not necessary it is recommended that you disconnect from your VPN connection.
To use VPN Service on your Ubuntu OS installed device follow these steps:
VIA 3.1.0 for Linux introduces support for Ubuntu 18.04 LTS but Ubuntu 12.04 LTS is not supported anymore. 
Before you install or upgrade to VIA 3.1.0 for Linux, the following packages must to be installed on the client device:
libqtcore4
libqtgui4
libgnome-keyring0
These packages are available for download from packages.ubuntu.com, and can be installed on the device using the command sudo apt install <package name>. When you first install or upgrade to VIA 3.1.0 for Linux, the application does not start automatically, and must be opened manually by selecting the VIA application link on the desktop. If the warning message untrusted application launcher appears, select the trust and launch option.
Login to netregister.metu.edu.tr
Click VPN service and download the installation file for your Operating System.

Run the installer and Click Next, Install buttons where applicable. Enter your password for administrative tasks. 

When the installation has finished, enter border.metu.edu.tr as Remote Server and your METU username and password into the fields as your connection credientials. Click Login.
 
Select default profile.
Service will open as Not Connected. If you want to Connect you can initiate a VPN connection by clicking Connect button on Connection Details tab.

 


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-use-metu-vpn-service-ubuntu-os-installed-devices

---

## Entry 2567

Question: How can i use METU VPN Service on Windows OS installed devices?
Answer: 


With METU VPN Service, by installing a packaged program (VPN Client) on personal computers and/or mobile devices, our members and students could access to our campus network resources when they are outside the campus.

Warning: For users using VPN, the connection speed per user is defined as 8 Mbps. For this reason, in the cases that VPN connection is not necessary it is recommended that you disconnect from your VPN connection.
To use VPN Service on your Windows OS installed device follow these steps:
Login to netregister.metu.edu.tr
Click VPN service and download the installation file for your Operating System.
Then start the setup process.


On the first screen click on Next option to start the setup process. Then continue by clicking Next buttons.




After you check the License Agreement, click on Next button.











After you choose where to setup VPN software, click on Next button.

Continue to setup by clicking on Install button.


Click on Finish button to finish installation process.

After the VPN software launched, Click on "Click to download VPN profile" button.

Then fill in the blanks accordingly. You should write border.metu.edu.tr in the field Enter VPN Server URL. When you finish, click on Download button.

Select default profile.


Then write your METU username -which is like e000000 (or your usercode if you are a METU personnel)- in the Username field and write your password in the Password field. When you finish, click on Proceed button.

Now you are connected to Metu VPN Network.After your login, application may be minimized into System Tray. You can bring the application to the foreground by double clicking. When you finish your work with Metu VPN connection you can right click on the symbol of the software in System Tray and click on Disconnect option.
If you are having issue with VPN program and connection you can visit https://faq.cc.metu.edu.tr/faq/i-cannot-connect-vpn-service-even-if-i-en... and https://faq.cc.metu.edu.tr/faq/i-have-problems-installing-vpn-services-w... addresses to get more information.  


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-use-metu-vpn-service-windows-os-installed-devices

---

## Entry 2568

Question: How many total users can use METU VPN Service at the same time?
Answer: 

1000 users can use the METU VPN Service at the same time.


Link: https://faq.cc.metu.edu.tr/faq/how-many-total-users-can-use-metu-vpn-service-same-time

---

## Entry 2569

Question: How to Delete VPN Profiles ?
Answer: 

Open Aruba VIA and click "Settings" icon.

Click on "VPN Profiles" tab and click  "Clear Profiles".

Select current profile "UserController1" from the list and click  "-" icon.

Confirm the process. Click  "Continue".

Click  "Cancel" to return "VPN Profile Download" section.

"Click to download VPN Profile".

Enter the "border.metu.edu.tr" url. Click  "Download" button.

Select "default" profile from the list. 

Enter your "username" and "password". Click  "Proceed". Download the profile.

Reboot your computer and open again Aruba-VIA. Enter your "username" and "password" to connect METU VPN.



Link: https://faq.cc.metu.edu.tr/faq/how-delete-vpn-profiles

---

## Entry 2570

Question: How to Download the VPN Application?
Answer: 

To download the VPN application, please visit https://netregister.metu.edu.tr and click "VPN Service" icon.

In the VPN Service menu,  please click "Download" or "View" link to download  the VPN application which suits your Operating System.



Link: https://faq.cc.metu.edu.tr/faq/how-download-vpn-application

---

## Entry 2571

Question: I cannot connect VPN Service even if I entered my user code and password correctly. What could be the problem?
Answer: 

First of all, please check your user code and password combination using https://useraccount.metu.edu.tr/. You can also specify recovery e-mail address from that page. If user code and password combination is not the case, VPN Client profile could have been changed. Therefore, you are advised to remove the VPN connection profile from your device. You can clear saved profiles from your VPN Client or you can re-install the VPN Client program. If your problem persists, please visit http://faq.cc.metu.edu.tr/faq/i-have-problems-vpn-services-what-can-i-do


Link: https://faq.cc.metu.edu.tr/faq/i-cannot-connect-vpn-service-even-if-i-entered-my-user-code-and-password-correctly-what-could-be

---

## Entry 2572

Question: I have problems with VPN services, what can I do?
Answer: 

If you have problems with installing the Aruba VIA software, please visit https://faq.cc.metu.edu.tr/faq/i-have-problems-installing-vpn-services-w...
If you have problems with connecting to the VPN service, please check the following settings:
Make sure that you have the version of Aruba VIA installed on your system is the same as the one available from https://netregister.metu.edu.tr . There may be an update to the version you are using. After downloading the new version, follow the steps at http://faq.cc.metu.edu.tr/groups/vpn-service matching your operating system to setup Aruba VIA.
If you end up with "... has stopped working" Windows error message when you try to run Aruba VIA software, there might be a problem with the software installation or a different problem with the operating system. For this problem, you can follow the resolutions suggested from this link. 
For each connection, you need to provide your usercode and password. If the Aruba VIA application does not ask for your usercode and password, please try clearing the profile of Aruba VIA. You can follow the steps at http://faq.cc.metu.edu.tr/groups/vpn-service matching your operating system to setup Aruba VIA.
Your network provider might be blocking the communication ports Aruba VIA needs to use. The ports Aruba VIA uses are 443 and 4500. (UDP:  500, 1701, 4500 TCP: 1723, 443, IP protocol: 50 are also used for MACOS) You can contact the IT department of your network provider to make sure that these ports are not blocked.
Any antivirus or firewall applications installed on your computer might also block VPN connections or cause the application not to install. In such a case, please uninstall both the VPN and the antivirus/firewall applications and restart your computer. Then, you can try installing Aruba VPN. If you can establish the connection, you can install the antivirus after the VPN application. (During our trials, in Windows 10 64 bit running Symantec Endpoint protection, even if the real-time protection is disabled, the VPN application and setup failed. With both Symantec and Aruba VPN uninstalled and then only Aruba VPN installed, VPN connection can be established)
If you cannot see the Aruba Via driver in the Device Manager / Network adapters, it means that the setup of Aruba VPN is not complete and VPN might not work as expected. In such a case please uninstall and try installing Aruba VIA again and make sure that Aruba Via Driver is working properly in Device Manager.
You can only connect to the VPN service with the clients available from https://netregister.metu.edu.tr/ and for the listed operating systems. Due to the protocols used, you cannot connect to the VPN service with the utilities built-in the operating system or any other third party clients. If there is not an Aruba VPN client available, you can connect to the VPN via other devices till a version compatible with your operating system becomes available.
Even after trying the above recommended solutions, please open an issue via https://itsupport.metu.edu.tr/
 
Usercode:
Operating system and device type (PC, Tablet, Phone, etc.):
Screenshot of diagnostics tab:
Screenshot of Connection Log in Diagnostics tab:
Screenshot of the errors, if any, in Connection Details tab
The logs created with the Send Logs button in Connection Details tab:
Time / date you try to connect


Link: https://faq.cc.metu.edu.tr/faq/i-have-problems-vpn-services-what-can-i-do

---

## Entry 2573

Question: My password is not asked when I try to connect VPN Service. What Should I do?
Answer: 

When you are connecting to the VPN Service, you should enter your password on each connection. If you are not asked to enter your password everytime, you are advised to remove the VPN connection profile from your device. You can clear saved profiles from your VPN Client or you can re-install the VPN Client program. 


Link: https://faq.cc.metu.edu.tr/faq/my-password-not-asked-when-i-try-connect-vpn-service-what-should-i-do

---

## Entry 2574

Question: How is METU Wireless Network managed?
Answer: 

METU Wireless Zones

 


Link: https://faq.cc.metu.edu.tr/faq/how-metu-wireless-network-managed

---

## Entry 2575

Question: Is there a wireless network in METU, how can I connect?
Answer: 

History of Wireless Network in METU
Middle East Technical University Computer Center has been the first to deploy wireless network among Turkish universities. This network was setup in point-to-point mode with 802.11b standard. Four distant departments / administrative units were connected using this method.
A set of wireless connection equipment was set a side for emergency cases, in case the connection of a department might be damaged and there would be a need of immideate connection. This set was used a couple of times to connect the department/unit whose connection was damaged, to the backbone network temporarily until the connection is reestablihed conventioanlly.
Later in year 2003, the first workgroup mode wireless network was established at the top of Central Engineering Building for enabling mobile clients' connectivity to Internet.
The present of Wireless Network in METU
In year 2005, with the increase in number of the wireless clients, the coverage area of the workgroup wireless network METU had been expanded to cover nearly the whole departments and administrative units. In every department and unit, hot spots for mobile users had been determined and these spots had been covered with wireless networks by setting up 802.11g access points. Now there is at least one wireless coverage area in every department and in addition to these, part of the dormitories, all academic residences, all the halls of the Library and the Cultural and Convention Center, and the guest houses are under coverage. To see the map of the wireless network points in METU you can take a look this map.
There is currently at least one SSID broadcast in every AP (ng2k broadcast, which is available without any encryption, ended in 2018 and meturoam has started). There is also a second SSID broadcast (namely eduroam) from that runs with 802.1x and that's a part of the EDUROAM, which stands for Education Roaming. EDUROAM runs on a RADIUS-based infrastructure that uses 802.1X security technology to allow for inter-institutional roaming. For more information about this network and the details of how to set it, please go to eduroam page.
Users without a wireless network interface card can borrow cards from the Library and Cultural and Convention Center with their ID cards. Unfortunately this service is available to METU students and personnel only. These cards are introduced to the authentication system beforehand and needn't to be registered.
People visiting METU can use the wireless service at Cultural and Convention Centre and guest houses by registering their MAC addresses. This is going to be temporary registeration and will be deleted after a predetermined time.
 


Link: https://faq.cc.metu.edu.tr/faq/there-wireless-network-metu-how-can-i-connect

---

## Entry 2576

Question: It seems I have a connection to the wireless network but I can't connect to the Internet. What should I do?
Answer: 

Wireless network connection problems are observed in some of Android devices using Android 6 and prior versions. Occasionally these devices display there is an established wireless connection on the screen but when you try to connect to the Internet, they fail. This problem is originated from a bug in the operating system. The bug cause Android devices to continue to use DHCP-leased IP addresses after the leases expire, and cause Android devices to resume using IP addresses from expired DHCP leases. When you face the the same problem please disable your Wi-Fi connection and enable it again.


Link: https://faq.cc.metu.edu.tr/faq/it-seems-i-have-connection-wireless-network-i-cant-connect-internet-what-should-i-do

---

## Entry 2577

Question: metuconnect
Answer: 

If you do not have a password for meturoam and do not have access to METU wireless network, then you can connect to metuconnect SSID in order to connect to meturoam. After connecting to metuconnect, please login to https://netregister.metu.edu.tr and follow the instructions to create a new meturoam password. Users who already have meturoam passwords do not need to connect to metuconnect.
There are access restrictions in the metuconnect network.


Link: https://faq.cc.metu.edu.tr/faq/metuconnect

---

## Entry 2578

Question: My internet connection is very slow. What could be the problem?
Answer: 

If your wireless internet connection is slow, you can review the following items;
- Use of wrong modeled and outdated wireless ethernet card driver- Use of shields to cover the antennas of mobile devices or computers (especially metal ones)- Use of computer or device far away from the wireless access point (distance and intervening obstacles will reduce performance)- Having internet access in places with high user density (performance will decrease as the number of users on the wireless network access point increases). When using a wireless network, if possible, places with fewer users around can be preferred.- Unnecessary applications that make download/upload operations when using a wireless network (for example, downloading files while using Zoom)- Meturoam/Eduroam are virtual wireless network broadcasts and both are broadcast from physically the same wireless network devices. Some devices may experience problems because they use different crypto technologies. Alternatively, a connection can be attempted with the other.- Metuconnect is a network open for authorization only and does not provide an Internet connection. You can only reach netregister.metu.edu.tr via this network. After completing your authorization procedures, you need to stop using it by "forget this network". Staying connected to this network will cause you to experience Internet problems.- Staying between two similar broadcasts can cause connection problems, as mobile devices in wireless networks "roam" in a way that prefers the better one among the available broadcasts. Moving closer to one, if possible, will help eliminate these problems.- Current wifi technologies operate in the 2.4 and 5Ghz bands. 2.4Ghz performs much better in terms of wall throughput and distance. But considering the bandwidth and the number of users, 5Ghz works much better. If the features of your device are suitable, you can check which one you are connecting from. In some devices, one may be given priority or the device may be forced to use only one of them. In cases where you are close to a wireless network access device, providing a 5Ghz connection will increase performance. If you are far away from the device or there are walls in between, setting 2.4Ghz will provide a more stable connection.
The slowness of your wired/wireless network connection speed may be due to any of the issues mentioned in the control items above. In addition, the connection speed may be slow due to the problem with your computer (problems with your network interface card, virus, etc.).
When it is said "I have a problem with my internet speed", it is very important to define the problem correctly for a solution. Information such as the page trying to connect, the device used during the connection (operating system and MAC/IP address information), the connection time interval, the connected user code are very important for a quick solution. The address https://speedtest.metu.edu.tr/ can be used to detect the slowness of the connection speed and see the instant speed.


Link: https://faq.cc.metu.edu.tr/faq/my-internet-connection-very-slow-what-could-be-problem

---

## Entry 2579

Question: What are the METU Wireless Network Rules and Regulations for Use?
Answer: 

1. The use of wireless network resources (network connection, wireless network connection card, campus /off-campus access etc.), which are allocated for METU students and members, is subject to the rules and conditions set forth within "METU Computing and Networking Ethics" which is available at this address .
2. The state allocates and grants to the University financial resources in order to accomplish essential computer networking technology investments that will primarily aid the instructional, academic, research and administrative objectives of the University. The personal use of the wireless network facilities by the users should in no way disrupt access priorities of those users that use the network for such instructional, academic, research and administrative objectives. In this respect, the users can find theguidelines for the appropriate use of network resources, the rules and regulations that the users must comply with and misconducts & prohibited behaviours as below:
 KaZaA, iMesh, eDonkey2000, Gnutella, Napster, Aimster, Madster, FastTrack, Audiogalaxy, MFTP, eMule, Overnet, NeoModus, Direct Connect, Acquisition, BearShare, Gnucleus, GTK-Gnutella, LimeWire, Mactella, Morpheus, Phex, Qtella, Shareaza, XoLoX, OpenNap, WinMX, DC++, BitTorrent etc..
a. Peer-to-peer (P2P) file sharing programs, as well as violating copyright and licensing rules, use up an excessive amount of bandwidth that consequently hinders the use of network resources for purposes of priority. For this reason, it is strictly forbidden to use the "peer-to-peer" file sharing programs - even if they are used inside the campus network. Such usage includes, but is not limited to, the following programs:
b. It is expressly forbidden to use wireless network resources for commercial purposes or for activities of personal gain.
c. It is forbidden to use wireless network resources for mass mailing, mail bombing, sending spam and users are not allowed to provide the means to the third parties to perform similar acts.
d. It is prohibited to keep possession of server computers that provide internet service (web hosting service, e-mail service etc.) via wireless network.
e. Users must not intentionally allow others to use University network resources from outside or, in other words, users must not pave the way for others to exploit privileges and act as if they are authorized to own the legitimate rights of the University users. (proxy, relay, IP sharer, NAT etc.)
f. It is forbidden to commit activities that threaten the security of the network (DoS attack, port-network scan etc.)
g. Users are definitely not allowed to change the hardware address (MAC address) of wireless network interface. This address is only to be handled and verified to the authentication system of METU Computer Center (CC) by the CC Network Group. If changing the MAC address is inescapably required (as in the cases of breakdown or failure of wireless network access card etc.) users must certainly report it to Computer Center to carry out the proper procedure for that change. (The computer will not gain access to the wireless network, unless its new MAC address is authenticated by the authentication system).
h. Wireless network facilities of the University (network connection, user codes, local/off-campus access etc.), which are granted as a privilege to the University members, will be used by every user in an appropriate, legal, ethical and considerate manner in accordance with the codes of behaviour and the regulations. It is the sole responsibility of all users that they are not endangering the safety of the resources by providing intentionally or unintentionally the means tothe third parties to access to network resources. The user alone is answerable and accountable for every unlawful and unwanted consequences that may result from this act.
3. If the use of the compurting and networking facilities is proven to be incompatible with the educational and scholarly missions of the University, and if the user has been proven to behave irresponsibly, inappropriately and illegally in a manner displaying disruptive and inappropriate conduct that endanger the efficiency, integrity, safety and continuity of networking services; and if the user breaches the rules and regulations set forth in this document, one or more of the following disciplinary actions may be taken as a reasonable response to eliminate threatening and abusive behaviour;
local and/or off-campus network access privileges may be restricted,
local and/or off-campus network access privileges may be suspended, modified or witheld,
the user codes and user accounts on the central server systems may be terminated,
University's disciplinary mechanisms such as investigation or prosecution may be initiated, judicial proceedings may be started,
4. the student, who has been proven to have disregarded or violated the rules and regulations, will be forewarned the departmental secretary.
5. These rules and regulations become effective as soon as they are publicized. The University and Computer Center reserves the right to amend these Rules and Regulations at any time without prior notice. The updated version of the rules and regulations can be viewed at this web address.
NOTICE of DISCLAIMER:
METU CC does not accept any responsibility of the risks that arise from utilization of the wireless network. All responsibility belongs to the user.


Link: https://faq.cc.metu.edu.tr/faq/what-are-metu-wireless-network-rules-and-regulations-use

---

## Entry 2580

Question: Which devices are known NOT to support meturoam?
Answer: 

A device must support WPA2 Enterprise with PEAP/MSCHAPv2 in order to be able to connect to METU wireless network, meturoam. The following devices that are known to NOT work on the meturoam wireless network.
Kindle Wi-Fi or Wi-Fi + 3G
Xbox 360 S or Xbox wireless networking adapter
Sony Playstation 3 and Sony PSP
Nintendo Wii U, Nintendo Wii, Nintendo DS, Nintendo DSi and Nintendo 3DS (known to not work on any network)
Apple TV 1st and 2nd Generation
Nook v1.5
Roku HD/XD/XDS Streaming Player
TiVo Wireless Network Adapter
 


Link: https://faq.cc.metu.edu.tr/faq/which-devices-are-known-not-support-meturoam

---

## Entry 2581

Question: Can I load money to my smartcard by using foreign bank card? 
Answer: 

You can get an error message while you are loading money to your smartcard with your foreign bank card. You may contact with your bank to check it.


Link: https://faq.cc.metu.edu.tr/faq/can-i-load-money-my-smartcard-using-foreign-bank-card

---

## Entry 2582

Question: Can I transfer the virtual money left on my METU ID card back to my account?
Answer: 

Yes, you can transfer your virtual money back to your bank account. To do this, you should go to "muhasebe şefliği" department located in cafteria.  


Link: https://faq.cc.metu.edu.tr/faq/can-i-transfer-virtual-money-left-my-metu-id-card-back-my-account

---

## Entry 2583

Question: How can I load and spend money with SoliClub application? 
Answer: 

You can load money (balance) to your smartcard or spend money through QRCode located on turnstile at cefteria by using SloClub application devloped by Utarit company. You need to match your credit or debit card with BKM (Interbank Card Center) Ekspress in order to load/spend money through SoliClub application. By this means, you can load or spend money through your matched bank card. You also need to tap your smartcard to one of the kiosks or balance update terminals located at cafeteria in order to transfer loaded money (by using online systems) to your smartcard. You should have active smartcard in order to use SoliClub application for loading and spending money. If you are renewing your smartcard and haven't received your new smartcard yet, you can not use this application. Your new smartcard should be given to you in 3 or 5 working days. For any delay, you can get in touch with Student Affairs (if you are student) or Directorate of Personnel Department (if you are Metu personnel). You can reach extra information by clicking on the links below.
SoliClub Application Use
SoliClub Balance Load


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-load-and-spend-money-soliclub-application

---

## Entry 2584

Question: How can I load money through odtucard website?
Answer: 

1. Open https://odtucard.metu.edu.tr from your web browser and login with your student / personnel number. 

2. After you logged in system, enter the amount which you want to load to your smart card on the right side and click on "Load Money For METU Card" button.

3. Click "Yes" on the confirmation window.

4. Make a payment with your bank account information. Payment is done with 3D Secure thorugh odtucard website. So, your card should be open to pay with 3D secure. When this phase is terminated by closing the window, payment process is suspended by the sysytem and you should wait a period of time to make a payment again.

5. After making payment with 3D secure, "provision is successful" message appears and after a while, you are directed to odtucard webpage. The amount you loaded to your smart card is seen on the "pending provision" field. In order to transfer the money to your smarcard, you should tap your card to one fo the kiosks or balance loading devices located in the cafeteria.
 


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-load-money-through-odtucard-website

---

## Entry 2585

Question: How can I see my cash payments and loadings?
Answer: 

You can see your cash loadings/payments from “Transaction/Kart Hareketleri” section on https://cardinfo.metu.edu.tr web page after you logged-in the system. 


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-see-my-cash-payments-and-loadings

---

## Entry 2586

Question: I am a METU staff. Can I get an ID card for my relatives?
Answer: 


 Yes. You can get an ID card for your children and wife/husband if you are an academic or administrative personnel. You can find related information from https://ihm.metu.edu.tr/tr/akilli-kart web address.

 




Link: https://faq.cc.metu.edu.tr/faq/i-am-metu-staff-can-i-get-id-card-my-relatives

---

## Entry 2587

Question: I cannot get in/out at the electronic card pass system of the departments. What should I do?
Answer: 


If the card reader does not give a ‘beep’ warning even though you hold the card from a few centimeters distance of the card reader with the METU logo, it means that there is a physical problem with your card. If you are a METU staff, apply to the Directorate of Personnel Affairs, if you are a METU student apply to the Student Affairs Office where you can have your card checked and you can apply for a new card if it is necessary.



If the card reader gives a ‘beep’ warning but the door does not open, then there may be a problem with your authorization. You can apply to the authorization officer of your department and have your authorization checked for access. 
The access authorization is granted by the department officer(s) and you can get information about your authorization status from them. If you previously were able to pass and are experiencing the problem just this time and/or if there are multiple people experiencing the same problem, possibly there is a malfunction with the smart card system. Firstly, you can inform your department authorization officer. If your authorization is still not defined, you can report the problem via  IT support page by using your user account information. 
 




Link: https://faq.cc.metu.edu.tr/faq/i-cannot-get-inout-electronic-card-pass-system-departments-what-should-i-do

---

## Entry 2588

Question: I get a warning message says “Your smart card has been canceled/out of use. Please apply your University” What should I do?
Answer: 

Your smartcard might have been canceled since you’re retired/graduated or your working period has finished. If one of these conditions does not fit your case and you still get this message, you can apply to Student Affairs Office if you are a student and to Directorate of Personnel Affairs if you are a METU staff.


Link: https://faq.cc.metu.edu.tr/faq/i-get-warning-message-says-your-smart-card-has-been-canceledout-use-please-apply-your-university

---

## Entry 2589

Question: I have changed my Smart ID card. Do I have to reactivate my new ID card?
Answer: 


No. Your new Smart ID card is provided you as the system recognize it, you can use your new smartcard upon receiving it.
 




Link: https://faq.cc.metu.edu.tr/faq/i-have-changed-my-smart-id-card-do-i-have-reactivate-my-new-id-card

---

## Entry 2590

Question: I have graduated. Would the available cash on my revoked card be returned to me?
Answer: 

No.


Link: https://faq.cc.metu.edu.tr/faq/i-have-graduated-would-available-cash-my-revoked-card-be-returned-me

---

## Entry 2591

Question: I have loaded money to my smartcard from online balance loading sysytem (odtucard), the amount I have loaded has not been transferred to my smartcard. What should I do?
Answer: 

When you load cash to your smartcard during launch hours (after 11:00 a.m.) you should tap your card to load/update devices or Kiosks in order to transfer upload amount to your smartcard (the images are below). If the amount has not been transferred despite you tap your smartcard to mentioned devices, you can report your problem from Metu Computer Center IT Support page by using your user account information. 
              


Link: https://faq.cc.metu.edu.tr/faq/i-have-loaded-money-my-smartcard-online-balance-loading-sysytem-odtucard-amount-i-have-loaded

---

## Entry 2592

Question: I have lost my smartcard and apply for a new one, after a short time I found my lost smartcard. What can I do?
Answer: 

When you have lost your card and apply for a new one (with lost/stolen card option), your lost smartcard is automatically set to passive mode so that no one can not use it. If you find your lost card before your new card is printed, you can apply for a Computer Center (B-14 Office). After your card is controlled and seen as working, then it can be set to active mode again if only your new card application is not in print process. 


Link: https://faq.cc.metu.edu.tr/faq/i-have-lost-my-smartcard-and-apply-new-one-after-short-time-i-found-my-lost-smartcard-what-can-i

---

## Entry 2593

Question: I'm the person who is responsible for authorization of people to department/unit e-gate system. How can I access to  related interface for e-gate authorization?
Answer: 

The person who is responsible for authorization of people to department/unit e-gate system can access to related interface (web page) by using the links provided below according to founded e-gate system and they can also make authorization of people to related e-gates. Since there is a restriction of authorized people (Department/Unit IT Coordinators) by their IP addresses to related interfaces, you can request your access demands to these interfaces through hotline (hot-line@metu.edu.tr).
Furthermore, we recommend you to add these links to your web browser's bookmark list.
BOTT E-Gate System
UTARIT E-gate system


Link: https://faq.cc.metu.edu.tr/faq/im-person-who-responsible-authorization-people-departmentunit-e-gate-system-how-can-i-access

---

## Entry 2594

Question: In case of the need to change my Smart ID card, would the virtual money on my old card be transferred to my new ID card?
Answer: 

When you change your smartcard because of various reasons (loss, stolen, broken, impairment etc.) the virtual money kept in your old smartcard is automatically transferred to your new smartcard. To do this, you need to tap your new card to one of the cash loading kiosks located in Cafeteria.
If you face with any problem, you can make your smartcard examined by related departments by stating your problem via METU CC - IT Support webpage after you logged in with your user account information. 


Link: https://faq.cc.metu.edu.tr/faq/case-need-change-my-smart-id-card-would-virtual-money-my-old-card-be-transferred-my-new-id-card

---

## Entry 2595

Question: METU Smartcard History
Answer: 


The Smart Card Technology, which has been under development since the early 2000s in METU, was put into effect as a project at the start of the 2002 - 2003 academic year when all students and staff were provided with Smart Card identification cards. 
Within the scope of the project, as planned, the Smart Card was put into use firstly as the e-wallet for the cafeteria, then as an e-ID application at seven department buildings, two PC rooms, and two campus gate entry barriers in 2005. 

With the second stage of the Smart Card application, started at the end of 2006, the e-wallet application of the smart card has been extensively widespread within the campus. Later stages of the project is being devised and shaped according the needs and the requirements of the METU members. All information regarding the Smart Card project may be accessed at our web pages.


Link: https://faq.cc.metu.edu.tr/faq/metu-smartcard-history

---

## Entry 2596

Question: My cash/credit card does not have e-commerce property, what should I do?
Answer: 

In order to load cash to your smartcard, your cash/credit card should have e-commerce property. You can make a contact with your bank to activate e-commerce property. 


Link: https://faq.cc.metu.edu.tr/faq/my-cashcredit-card-does-not-have-e-commerce-property-what-should-i-do

---

## Entry 2597

Question: My Smart card has been changed. Would the available cash on my old card be transferred to my new card?
Answer: 

When your smart card is changed, the virtual money available on your old card which you loaded from the cash loading kiosks or odtucard is transferred to your new card automatically.  To do this, you need to tap your new card to one of the cash loading kiosks located in Cafeteria (the image is below).
If you realize a problem about the money transfer you can visit METU CC - IT Support page. After you login into the system, you can report your issue via opening a new issue. 



Link: https://faq.cc.metu.edu.tr/faq/my-smart-card-has-been-changed-would-available-cash-my-old-card-be-transferred-my-new-card

---

## Entry 2598

Question: My smartcard is broken, what should I do?
Answer: 

When your smart ID card is broken or physically damaged, your smart ID card is changed for a certain fee. To renew your ID card, you can apply for a new card by using cardinfo website (https://cardinfo.metu.edu.tr/). To take your printed new card, you can apply to your department secretary if you are a student and to your unit secretary if you are a METU staff. You can get information about the documents required to apply for a new ID card from related offices.


Link: https://faq.cc.metu.edu.tr/faq/my-smartcard-broken-what-should-i-do

---

## Entry 2599

Question: My smartcard is lost/stolen. What should I do?
Answer: 

When you realize that your smartcard is lost/stolen, you should cancel your ID Card from cardinfo.metu.edu.tr internet address. In that case, your smartcard is cancelled by the system. 


Link: https://faq.cc.metu.edu.tr/faq/my-smartcard-loststolen-what-should-i-do

---

## Entry 2600

Question: The information displayed on the screen of the Cash payment/load devices does not belong to me. What is the reason?
Answer: 

If you see different name/surname when you scan your smartcard to payment or load devices, your smartcard might have been formatted wrongly. If you are a METU staff, apply to the Directorate of Personnel Affairs, if you are a METU student apply to the Student Affairs Office where you can have your card checked and you can apply for a new card if it is necessary.


Link: https://faq.cc.metu.edu.tr/faq/information-displayed-screen-cash-paymentload-devices-does-not-belong-me-what-reason

---

## Entry 2601

Question: The refund that I requested has still not been loaded to my smart card. What could be the problem?
Answer: 










The refund amount is loaded to your debit/credit card whose IBAN number you have provided during refund process, instead of smardcard itself. Duration might delay by depending on confirmation of related departments. 
 


Link: https://faq.cc.metu.edu.tr/faq/refund-i-requested-has-still-not-been-loaded-my-smart-card-what-could-be-problem

---

## Entry 2602

Question: Virtual money that I have deposited on my smartcard was set to zero just after I deposited or after I used it for a few times. What should I do?
Answer: 

When the virtual money in your smart ID card is deducted from your account disproportionally compared to your uses, you can visit METU CC IT support page. After you login into the system, you can report your issue by opening a new case. In that case, it is necessary to make contact with relevant departments for the card to be examined and if the problem is determined, your money is paid back to your account.


Link: https://faq.cc.metu.edu.tr/faq/virtual-money-i-have-deposited-my-smartcard-was-set-zero-just-after-i-deposited-or-after-i-used

---

## Entry 2603

Question: When I tap/scan my smartcard to payment/load devices I get an error message says “your card has not been read” or “your card has not been recognized”. What should I do?
Answer: 

You need to scan/tap your smartcard to payment/load devices at most 3 cm distance (approximately 2 fingers). Furthermore, you need to wait till the device read your card before you draw back your card (approximately 3 seconds).
 


Link: https://faq.cc.metu.edu.tr/faq/when-i-tapscan-my-smartcard-paymentload-devices-i-get-error-message-says-your-card-has-not-been

---

## Entry 2604

Question: When is the money in smart ID card transferred back to my bank card if the smart ID card is cancelled?
Answer: 

When your smartcard is cancelled, you should apply to accounting department located in the Cafteria in order to take your virtual money back to your debit/credit card. Depending on confirmation of related departments, your virtual money is paid back to your bank account in approximately 15 working days.


Link: https://faq.cc.metu.edu.tr/faq/when-money-smart-id-card-transferred-back-my-bank-card-if-smart-id-card-cancelled

---

## Entry 2605

Question: Under which circumstances would a user account be terminated?
Answer: 

Student User Accounts are terminated one (1) term after graduation. The user codes of the exchange students who are in the Erasmus or Special Student category are activated for one semester and are terminated automatically at the end of the semester. After the data of the termination processes are processed and before the termination date at particular times an e-mail informing the date of the termination is sent. Being effective from the 2003-2004 academic year graduated students, the e-mail addresses of the graduated students in the exxxxxxmetu.edu.tr format which are defined on the METU CC central servers are directed to another desired e-mail account. An information e-mail about the redirection services is sent one month before the student would able to use the service. For more information on e-mail forwarding, please visit https://faq.cc.metu.edu.tr/faq/how-can-i-use-metu-e-mail-forwarding
User account of the staff who left the university due to resignation, being dismissed or off-duty are terminated after 3 months. If desired, METU e-mail addresses of those who left the university may be redirected to another e-mail address. For more information on e-mail forwarding, please visit https://faq.cc.metu.edu.tr/faq/how-can-i-use-metu-e-mail-forwarding User codes of the leaving staff may be terminated immediately if requested by the administrative supervisor of the related unit.
The user accounts of the part-time academic members are terminated at the end of an academic year unless their departments prolong their employment. The user account of the retired staff is not subject to termination.
The temporary user accounts which are activated under the conditions specified by CC, are terminated at the end of their given period.
The user account of the deceased user is terminated.
The accounts of the units which are in the context of EIS Project and the student groups are only terminated if an official requirement is made by the related units or groups, if not these accounts are kept active.
Terminating the user account due to misuse:
In accordance with Information Technology Resources Usage Policies memorandum released on 24 March 2004;
In the case of the use policies as may be required
In the case of illegal uses defined by local laws
In the case of the limit exceeding of the temporary accounts
In the case of non-academic, commercial and/or illegal activities uses
When personal accounts are detected to be used by different persons instead of the users of the accounts.
In the case of detected attempts of acquiring/stealing the passwords, intervention to the files, changing them etc. of the other users registered on Server Systems.
In the case of the detection of unlicenced, illegal software on the allocated disk space of the user account
When the system integrity, security and the continuity of the service is obstructed
user accounts are terminated temporarily by the CC without notice. In the cases th user account would be permanently shut down, the user is notified beforehand. An user account which has been terminated by the CC due to improper usage may be kept inactive while disciplinary investigation and legal action proceeds, and the user account is reactivated only when the investigation procedure is over and the defense is accepted by the CC.
The University Administrative Board Decision on user code termination is available at the CC web page.


Link: https://faq.cc.metu.edu.tr/faq/under-which-circumstances-would-user-account-be-terminated

---

## Entry 2606

Question: Can I change my e-mail address that consists of my name and surname in the format 'name.surname@metu.edu.tr'?
Answer: 

In normal conditions you cannot change the e-mail address in the format name.surnamemetu.edu.tr that you have chosen from User Account Management web site on the address https://useraccount.metu.edu.tr.
However, if you change your name or surname by reason of marriage and divorce or as a result of a court decision, apply to Students Affairs if you are a student or to Staff Affairs if you are an international staff with your related documents. After they update your information, our systems will also be updated. 
If the e-mail address you will be given is in use by another user, you will be contacted in order to determine a new address.
Once your address is changed, the e-mails sent to your old e-mail address will not be forwarded to the new address and will be returned to sender. Relevant information procedure will be under your responsibility.


Link: https://faq.cc.metu.edu.tr/faq/can-i-change-my-e-mail-address-consists-my-name-and-surname-format-namesurnamemetuedutr

---

## Entry 2607

Question: How can I connect to the Central Server Systems from campus?
Answer: 

Within the METU Campus you can reach the central servers named Beluga and Orca.
_x0093_To connect central servers, you can use the newest version of SSH or try a different program. WinSCP is the one of the FTP programs you can use. You can make operations like changing the permissions of your files in the server, copying/moving a files and folders.
Additionally, for users who are more comfortable with command line PuTTY is a free software which enable to make necessary operations.
https://winscp.net/eng/download.php address can be used to download these two programs.


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-connect-central-server-systems-campus

---

## Entry 2608

Question: How can I connect to the Central Server Systems from off-campus?
Answer: 

In order to connect to the central servers from outside the METU campus using SSH Secure Shell Client you should first connect to the server named External (external.cc.metu.edu.tr). Once you connect to External, you can connect to Beluga or Orca using ssh command, such as;
ssh beluga.cc.metu.edu.tr


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-connect-central-server-systems-campus-0

---

## Entry 2609

Question: How can I create web pages by using my METU user account?
Answer: 

Please remember to act in conformity with METU Information Technology Resources Use Policy when you are creating web pages. To view these ethical codes, you can visit this adress.
The following steps will guide you when creating web pages on METU central servers.

Enter your user code/password and connect your computer to central servers (orca, beluga, rorqual and narwhal) by using SSH programs like PuTTY or WinSCP.


wwwhome directory is automatically created in your web user account. To check the file permissions of wwwhome directory, run the following command:
 ls -ald wwwhome 
The following line will be displayed after this command is executed. The first 10 characters (drwxr-xr-x) on this line indicate the file permissions of wwwhome directory and each character specifying the permissions must be the same with the permissions in the line below. (If the characters are different, you should repeat the process explained in step 2 (above) beginning from the command "chmod og=rx wwwhome".)
 drwxr-xr-x 14 uid gid 1536 Sep 20 12:10 wwwhome

In the next step, enter the following command to check the file permissions of your home directory.
 ls -ald ~ 
Check to make sure that the first 10 characters of the line displayed are the same with the characters indicated below:
 drwx--x--x 14 uid gid 1536 Sep 20 12:10 user-code
If the characters specifiying the permissions are different, you should run the following command:
 chmod a+x ~
If the steps above are carried out accordingly, the necessary directory structure would be created that will enable you to create your web page.


Let us create a sample introduction page. Open the wwwhome directory by entering the following command.
 cd wwwhome

Then, create an index.html file by entering the sample command below; (You may use the editor you are most comfortable with like, pico, vi etc.)
 pico index.html 
and enter the sample information below into this file.
 < html > < title >Home Page< /title > < h3 >Welcome< /h3 > < /html > 

Save the information in the index.html and close the file. To view your first page, write the following URL address in your active web browser (Netscape, Internet Explorer etc.) The URL address you will be using on your active web browser will be like the following sample address:
users.metu.edu.tr/user_code (personal users)www.*****.metu.edu.tr/ (web users)

You have just created your introductory web page successfully. Please remember to keep the information you will be using on your web page in the wwwhome under the home directory. The following URLs address to people at various levels and may include information, which may help you if you are creating a web page or intending to use HTML code.
Sites in English:
http://www.w3.org/MarkUp/Guide/ - Dave Raggett's Introduction to HTMLhttp://htmlhelp.org/ - HTML Help by The Web Design Group


And what's more, you can transfer the web pages you have created on your own computer via FTP (File Transfer Protocol) to your user account located on the systems and you can update the pages whenever you want in your account. It is important here not to forget specifying the file permissions of the files you will be transferring as "readable" by everyone. It will be easier for you to execute the following command and specify all the file permissions of the files accordingly in the end, i.e. after all your transfer operations are finished:
 chmod og=r file-name 

You can use various web editors while creating, updating and uploading your web pages.
 

Link: https://faq.cc.metu.edu.tr/faq/how-can-i-create-web-pages-using-my-metu-user-account

---

## Entry 2610

Question: How can I get an user account with @metu.edu.tr extension?
Answer: 

All user codes with @metu.edu.tr extension are assigned to a real person and these codes are given to the students with a student number or the personnel with a social security number.
METU Students
Students who have registered to the university and assigned a student number should visit useraccount.metu.edu.tr address. They should use "New Students" link and complete the form with the related information. After this process they can use their user codes with @metu.edu.tr extension. Aliases with @metu.edu.tr extension are not given for exchange students.  
ÖİDB tarafından kayıt işlemi gerçekleştirilen ve öğrenci numarası bulunan tüm öğrenciler useraccount.metu.edu.tr adresindeki Yeni Öğrenci bağlantısını kullanarak TC Kimlik veya Öğrenci numarası ile kayıtlı olduğu bölüm bilgisini seçer, beyan ettiği e-posta adresine Tek Kullanımlık Şifre iletilir. Bu şifre ile useraccount.metu.edu.tr adresine giriş yaparak kalıcı şifre, kurtarma e-posta adresi ve ad.soyad şeklindeki e-posta adresini (özel öğrenciler hariç) tanımlayabilir.
METU Personnel
The METU personnel should fill the F1 form which should be signed by the Department/Unit administration. They must apply to the Computer Center office B-14 with the form in person. All the users are obliged to obey to the "METU Information Technology Resources Use Policy".
No user code is provided for the users whose personnel ID number isn’t assigned by the METU Directorate of Personnel Affairs.


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-get-user-account-metuedutr-extension

---

## Entry 2611

Question: How can I recover the files I have mistakenly deleted from my user account?
Answer: 

In order to recover files deleted from your account by mistake, it ought to be enough just to fill out the form that you will see when you go to https://portal.metu.edu.tr/odtu_bidb/yedekleme/yedekleme.xhtml address and choose the date and folder that you want to recover. The system backs up the files in your account every night. You can recover the files that have arrived before back-up time and the files which have been deleted after back-up time. Note: Backup copies are kept for 30 days. 


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-recover-files-i-have-mistakenly-deleted-my-user-account

---

## Entry 2612

Question: How could i delete the files on the Central Servers?
Answer: 

By using rm –[options] <file name> command,you can erase any file you have selected.Sample options ;-e : Gives out information after the deletion of the file.-f : Deletes write protected files without asking for confirmation.(This option has no returning point, and should not be used unless required.)-I : Asks for confirmation before deleting the file.-r : Continuously deletes sub-directories without asking for confirmation.
For instance , by using :$ rm Bilgi-Islem*command, you can delete every file whose name begins with ‘’Bilgi-Islem’’.$ rm -rf denemecommand, you can delete the file named ‘’deneme’’ and its every sub-directory without any confirmation.


Link: https://faq.cc.metu.edu.tr/faq/how-could-i-delete-files-central-servers

---

## Entry 2613

Question: I am a METU personnel. How can I obtain a user code?
Answer: 

The METU personnel should fill the F1 form which should be signed by the Department/Unit administration. They must apply to the Computer Center office B-14 with the form in person. All the users are obliged to obey to the "METU Information Technology Resources Use Policy".
No user code is provided for the users whose personnel ID number isn’t assigned by the METU Directorate of Personnel Affairs.


Link: https://faq.cc.metu.edu.tr/faq/i-am-metu-personnel-how-can-i-obtain-user-code

---

## Entry 2614

Question: I am getting a “not authorized” message on the web page I have created by using my METU user account. What should I do?
Answer: 

If you are getting a "not authorized" message on the web page you have designed using your METU central user account, this means that there is a problem in right of access to the page. You can overcome this problem by using one of the methods below;
With Horde:
After entering Horde, from the top menu or from below the “my account” header, click on the file manager button. Select the wwwhome directory and click the change authorization option under the actions header and change authorization as seen below. Furthermore, you may check the access rights of the user home directory from the section next to the related directory.

By connecting to the server systems with Ssh:
In order to check the access rights of the wwwhome directory:
ls -ald wwwhome
Run the above command. A line like the below will come up after the execution of the command. The first ten characters (drwxr-xr-x) on this line indicate the access rights to the wwwhome directory and should have the same values as below.
drwxr-xr-x 14 uid gid 1536 Sep 20 12:10 wwwhome
 In case the characters are different, define the access rights of the wwwhome directory by running the commands below. 
 chmod og=rx wwwhome
Afterwards, in order to check the access rights of your home directory, type the command,
 ls -ald ~
 after which the below line will come up. Check that the first 10 characters have the same values as below:
 drwx--x--x 14 uid gid 1536 Sep 20 12:10 kullanici-kodu
 If the values are not as above, then run the command below:
 chmod a+x ~
When these steps are completed the necessary directory structure to be able to design a web page will have been built.

 


Link: https://faq.cc.metu.edu.tr/faq/i-am-getting-not-authorized-message-web-page-i-have-created-using-my-metu-user-account-what

---

## Entry 2615

Question: I get "Algorithm negotiation failed" error when I try to connect servers with SSH Secure Shell program. What can I do?
Answer: 

The version of SSH program you are using may not be supporting one of the encryption algorithms of the server. Therefore, you may get an error like “Algorithm negotiation failed”. For this reason, you can use the newest version of SSH or try a different program. WinSCP is the one of the FTP programs you can use. You can make operations like changing the permissions of your files in the server, copying/moving a files and folders.
Additionally, for users who are more comfortable with command line PuTTY is a free software which enable to make necessary operations.
https://winscp.net/eng/download.php address can be used to download these two programs.


Link: https://faq.cc.metu.edu.tr/faq/i-get-algorithm-negotiation-failed-error-when-i-try-connect-servers-ssh-secure-shell-program

---

## Entry 2616

Question: METUCloud
Answer: 

METUCloud service provides cloud storage and file sharing services to our users.
Our administrative/academic staff can use METUCloud service only in matters related to their fields of activity.
Personal files cannot be hosted in METUCloud storage.
In the METUCloud service, users are allocated 10GB of storage space by default.
Access to the service is provided through the address "https://metucloud.cc.metu.edu.tr" or the mobile application ("https://owncloud.com/mobile-apps/").


Link: https://faq.cc.metu.edu.tr/faq/metucloud

---

## Entry 2617

Question: My user account is closed. How can I get my e-mail backups (if there are any) and open them?
Answer: 

User accounts of our students whose studentships are suspended or over for any reason are closed after one (1) school term. Our users whose user accounts will be closed are notified about it with an e-mail at particular times.
Alumni’s e-mail addresses in exxxxxxmetu.edu.tr format identified by METU Computer Center central servers can be directed to another e-mail address requested. Information related to forwarding service can be found in https://faq.cc.metu.edu.tr/faq/how-can-i-use-metu-e-mail-forwarding address.
If you are not forwarded, since e-mails sent from other addresses won’t arrive after your user account is closed, there aren’t backups for sent e-mails after the closure date.
By logging into the e-mail account before the closure date, you can download your backups as a .mbox file to your computer as written on http://faq.cc.metu.edu.tr/faq/how-can-i-download-all-my-e-mails-horde
You can apply the methods below to see the e-mails sent to you via .mbox or tar.gz extended files and send it to another e-mail address of yours. As there is an extended tar.gz file that you downloaded to your computer, you can use 7-zip program to open it https://www.7-zip.org/ you don’t need such an opening program for .mbox file
In order to see the e-mails, you need to set up the Thunderbird program. You can follow the steps on https://www.thunderbird.net address for installation.
After you set up and open Thunderbird program, you must click Add-ons option from Settings part Add-ons section and set up ImportExportTools NG attachment on the pop-up window, by finding it from the search section. After the setup, Thunderbird client must be restarted. After it is restarted, create a new folder by right-clicking Local Folders at the left section and choosing New Folder. You can name it as you like.
In the sample below, we created a local folder named imported_mails.

Right-click the folder we have just created, from ImportExportTools NG menu: 
A) If you have a .mbox, by choosing Import mbox file, you can show your mbox extended file’s place and thus; reach your e-mails and direct it to another e-mail address, if you wish.

B) If you opened .tar.gz file with a zip program like 7-zip on a folder on your computer, you can continue with Import messages option. When you click Import messages option, first of all, you need to choose All files (*.*) as file type to display on the screen.
By choosing all files in related e-mail folders inside the taz.gz folder that you opened on the screen, you can make it visible on the Thunderbird client.
For example,>> Your e-mails that are in the Inbox are mails > INBOX > it’s inside of the cur folder. You may also access e-mail attachments seen on Thunderbird client from attachment section via this client and save on your computer.




Link: https://faq.cc.metu.edu.tr/faq/my-user-account-closed-how-can-i-get-my-e-mail-backups-if-there-are-any-and-open-them

---

## Entry 2618

Question: On which platforms can I use my METU user code and password?
Answer: 

You can use your user code and password;
to connect/reach to services provided by the METU-CC:
Reading E-mail (Horde, Squirrelmail, e-mail programs incorporating POP3/IMAP - https://faq.cc.metu.edu.tr/groups/e-mail-programs)
Accessing electronic lists (https://faq.cc.metu.edu.tr/groups/electronic-lists).
Designing web pages (https://faq.cc.metu.edu.tr/faq/how-can-i-create-web-pages-using-my-metu-...).
Using PC Rooms (http://pc-room.cc.metu.edu.tr) which are operated by the Computer Centre.
Our students can access Student Portal to register courses interactively or follow announcements and personal data. (https://student.metu.edu.tr).
Academic staff can access METU-SIS (https://sis.metu.edu.tr/)
Accessing Learning Management System (ODTÜCLASS - https://odtuclass.metu.edu.tr)
Utilizing METU Portal  (https://portal.metu.edu.tr)
Reaching most of services provided by METU units.
 


Link: https://faq.cc.metu.edu.tr/faq/which-platforms-can-i-use-my-metu-user-code-and-password

---

## Entry 2619

Question: Problems with User Accounts
Answer: 

If you experience problems during User Account creation, you can try some of the solutions below while getting a new user account from https://useraccount.metu.edu.tr
For alumni accounts, please contact mezunkart @ metu.edu.tr 
If you get CODE 103 error, please try again with another browser.
If you get CODE 182 error, please make sure that you selected the appropriate program. (Programs at Ankara campus and at NCC have different names.) Also make sure that you are registered to the active semester by the Registrar's Office.
If you get CODE 183 error, while creating your user code, an error occured, please reach us via "Contact Us" link on METU Computer Center web site with your usercode and related information, please attach a screenshot of the page if possible. 
Please use email addresses other than hotmail.com, live.com or outlook.com as there might be delays with METU - Microsoft e-mail systems.
If you accidentallay used such e-mail addresses, please check whether you received the activation message, check Junk / Spam folders as well. If you received the activation message, you can continue user code activation. If not, please contact us via "Contact Us" link on METU Computer Center web site with your student ID number (or TC ID) and related information.
Currently Registered Students
It is not neccessary to create a user account for currently registered users from User Account website. They can use their current username and password.
 
 


Link: https://faq.cc.metu.edu.tr/faq/problems-user-accounts

---

## Entry 2620

Question: What can I do from METU User Account Management page?
Answer: 

You can change your user account's password and define your recovery e-mail address to which your new password will be sent when you forget your password from the METU User Account Management page (https://useraccount.metu.edu.tr/).
In addition, the students who have newly registered to our University, should select their permanent password, recovery e-mail address and METU e-mail address before signing in central server systems.


Link: https://faq.cc.metu.edu.tr/faq/what-can-i-do-metu-user-account-management-page

---

## Entry 2621

Question: What to do, to make use of the services provided by the CC?
Answer: 

The academic/administrative staff who would like to work via the Central Systems or access the Internet should first fill out the User Code Application Form and have it authorized by the department/unit administrators and submit it to Room B-14 at the CC during working hours, presenting their ID card, in order to get their user code and password. Having this code the academic/administrative staff can; send and receive e-mail, affiliate in electronic communication lists or news groups, utilize the software which run on central systems or transfer files using FTP services. They may access any service available on the Academic/Student Information Services System.


Link: https://faq.cc.metu.edu.tr/faq/what-do-make-use-services-provided-cc

---

## Entry 2622

Question: When does a personnel user code expire and closed?
Answer: 

User accounts, which are closed due to reasons other than retirement or expired due to end of assignment, will be closed at the end of 3 months after the personnel leaves office. Back-up is available up to 1 year. The users should apply to METU CC IT Support Service (https://itsupport.metu.edu.tr/ with an ID card after specifying the date for back-up in order to getting the back-ups.
User accounts of the leaving personnel can be forwarded to another e-mail address. You can get more information via https://faq.cc.metu.edu.tr/faq/how-can-i-use-metu-e-mail-forwarding 
If valid reasons are stated, the user code can be prolonged for an extra 3 months. You can request prolongation via IT Support Service (https://itsupport.metu.edu.tr/)
The demands for more than 3 months (User code can be prolonged for 1 year up to approval of the head of the department/unit) should be approved by the head of department/unit by filling the F3 form. The form must be taken to the Computer Center B-14 office.
Research assistants whose duty term is over but the MS or Phd program persists, will be given 1 year prolongation until their education period is over.


Link: https://faq.cc.metu.edu.tr/faq/when-does-personnel-user-code-expire-and-closed

---

## Entry 2623

Question: How can I change my Alumni Account password? What should I beware of in picking a new password?
Answer: 



To change the password for your user code on Central Servers:
From the User Account Management Page:
Sign in to User Account Management web page with your user code and password from the address belowhttps://alumniaccount.metu.edu.tr Then click Change Password.
Users must create their passwords according to the following rules:
Mandatory elements in passwords are:
The password must be exactly 8 characters. Make sure there are no more or less characters.
The password must contain at least one uppercase letter (ABCD… .Z).
The password must contain at least one lower case letter (abcd… z).
The password must contain at least one number (1234567890).
The password must contain at least one of the special characters given in parentheses ([% () * +, -. /:; <> ^ _ {|} ~]).
Elements that should not be included in passwords are:
The password cannot contain a space character.
The password cannot contain 1900s or 2000s. (1978, 1999, 2001, etc.)
The password cannot contain consecutive numbers of 4 or more characters. (1234, 2345, 5678, etc.)
The password cannot contain characters that repeat itself more than 2 times. (AAA, zzz, etc.)
The password cannot contain Turkish characters. (ç, ğ, İ, ö, ş, ü…)
The password cannot contain non-ASCII characters. (ä, é, Ý, Ð, Π etc.)
The password cannot contain an easily predictable word or dictionary word, all uppercase or lowercase.
The new password cannot be the same as the last 5 passwords, if any.
Example passwords:
Polut36*
Dem70:ka
2K/mReD
2F,646(w
EO*A(/5y
.g1>4YjT
o)5aDA-9




Link: https://faq.cc.metu.edu.tr/faq/how-can-i-change-my-alumni-account-password-what-should-i-beware-picking-new-password

---

## Entry 2624

Question: I forgot my METU alumni user code password. Where can I apply?
Answer: 



You can get your new password if you add an alternate e-mail adress (password recovery/reset e-mail adress) using METU Alumni User Account Management https://alumniaccount.metu.edu.tr/ web page. To do so, you need to have a registered recovery e-mail. 
If you have a registered e-mail address, click on "Forgot password?” link
After filling the form, click on the “send e-mail” link. You should click the link sent to your e-mail address to reset and activate your new password.
If you remember your password and want to register a recovery e-mail address please log on to METU User Account Management page, click "REGISTER RECOVERY E-MAIL" link to register an e-mail address (other than your @metu.edu.tr address).




Link: https://faq.cc.metu.edu.tr/faq/i-forgot-my-metu-alumni-user-code-password-where-can-i-apply

---

## Entry 2625

Question: Password and Recovery E-Mail Procedures for METU Alumni User Codes
Answer: 



A- To change the password of your METU alumni user code:
Visit https://alumniaccount.metu.edu.tr/,
Log in with your current alumni user code and password you are using,
Click the CHANGE PASSWORD button on the following page,
Type your new password twice in accordance with the rules in Section E below and click the CHANGE button.
After a successful change, you can use your new password in a couple of minutes.
B- To set a new password in case you forget your password OR your password has been reset:
In case you forget your password, your recovery e-mail must be registered in your user account so that you can set yourself a new password. A new password activation link will be sent to your non-METU recovery e-mail address (Gmail, etc.) upon your request. You will be expected to reset your password within 24 hours via the link in the e-mail message. If your recovery e-mail is not defined in the system or if you have forgotten your recovery e-mail, follow the steps in sections C and D below.
If your recovery e-mail is defined in the system and you know your recovery e-mail;
Enter https://alumniaccount.metu.edu.tr/,
Under the User Login section, click "Forgot your password?"
Click on the "SEND E-MAIL" button after entering the "username", "recovery e-mail" defined in the system, and the "image verification" characters.
Check your recovery email address inbox. A new password activation link will be sent to your address. Click on the activation link on the next page.
When you click the activation link, you will be directed to the page where you can create a new password. When you create a new password in accordance with the criteria specified in section D, you will see the message that your password has been successfully changed.
After a successful change, you can use your new password in a couple of minutes.
C- To define a recovery e-mail:
Visit https://alumniaccount.metu.edu.tr/,
Login with the current user code-password you are using,
Click SET RECOVERY EMAIL button on the following page,
Write your recovery email and click the UPDATE button.
D- Our users should create their passwords according to the following rules:

Mandatory elements in passwords are:

The password must be exactly 8 characters. Make sure there are no more or less characters.
The password must contain at least one uppercase letter (ABCD… .Z).
The password must contain at least one lower case letter (abcd… z).
The password must contain at least one number (1234567890).
The password must contain at least one of the special characters given in parentheses ([% () * +, -. /:; <> ^ _ {|} ~]).

Elements that should not be included in passwords are:

The password cannot contain a space character.
The password cannot contain 1900s or 2000s. (1978, 1999, 2001, etc.)
The password cannot contain consecutive numbers of 4 or more characters. (1234, 2345, 5678, etc.)
The password cannot contain characters that repeat itself more than 2 times. (AAA, zzz, etc.)
The password cannot contain Turkish characters. (ç, ğ, İ, ö, ş, ü…)
The password cannot contain non-ASCII characters. (ä, é, Ý, Ð, Π etc.)
The password cannot contain an easily predictable word or dictionary word, all uppercase or lowercase.
The new password cannot be the same as the last 5 passwords, if any.
Sample Passwords:
Polut36 *
Dem70: ka
2K / mReD
2F, 646 (w
EO * A (/ 5y
g1> 4YjT
o) 5aDA-9




Link: https://faq.cc.metu.edu.tr/faq/password-and-recovery-e-mail-procedures-metu-alumni-user-codes

---

## Entry 2626

Question: Problems with Alumni User Accounts
Answer: 

If you experience problems during Alumni User Account creation, you can try some of the solutions below while getting a new user account from https://alumniaccount.metu.edu.tr/
If you get CODE 182 error, please make sure that you selected the appropriate program.
If you get CODE 183 error, while creating your alumni user code, an error occured, please try again later.
If you get CODE 184 error, entered e-mail does not match with the e-mail used in your application. Please be sure that you entered the same information you used in your application.
If you get CODE 185 error, you have already created your account.
Please use email addresses other than hotmail.com, live.com or outlook.com as there might be delays with METU - Microsoft e-mail systems.


Link: https://faq.cc.metu.edu.tr/faq/problems-alumni-user-accounts

---

## Entry 2627

Question: How can I download all of my e-mails with Horde?
Answer: 

With Horde, you can download the emails in a mailbox to your computer. For this, after logging in Horde web application in DYNAMIC mode, please right click on the mailbox you want to download and select Export / Dışa Aktar.

In the popup window, select "Download into a MBOX file" and click OK.

If you use Horde web application in BASIC mode, please use the Folders link, right below the NEW MESSAGE button, once you select the folder to be downloaded, click "Choose Action" menu and click Download.

You can also add your METU email address to email readers like Thunderbird or Outlook and online email services like gmail, hotmail, etc. Then, you can copy your email messages. For more information, please follow the links at http://faq.cc.metu.edu.tr/groups/e-mail-programs.


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-download-all-my-e-mails-horde

---

## Entry 2628

Question: How can I transfer files and folders between my METU user account and my computer by using Horde File Manager?
Answer: 

It is possible to transfer files between the central server systems and your personal computer by making use of the Horde File Manager. Once Horde is run, to perform the process you will have to choose the "File Manager" and "METU" under the "Others" menu.

In order to download a file resident on the central servers to your personal computer it is only necessary to click on the  icon. 
In the case of uploading a file in your personal computer to the central servers, using the section below the page, you should find the file you want to upload by clicking on the "Browse" button and once the file is chosen, click on the "Upload File(s)" button.


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-transfer-files-and-folders-between-my-metu-user-account-and-my-computer-using-horde

---

## Entry 2629

Question: How can I transfer files and folders between my METU user account and my computer securely?
Answer: 






To transfer files to your METU user account, please use file transfer software which support the secure FTP (sftp) protocol. (If you are not connected to the campus network, please use METU VPN. For more information on METU VPN, please follow this link.) In the connection settings, you can use beluga.cc.metu.edu.tr as the host/server and your usercode.
The following are some examples for the software which support secure FTP.
https://www.bitvise.com/ssh-client-download (Windows)
https://winscp.net/eng/download.php (Windows)
https://cyberduck.io (MacOS)







Link: https://faq.cc.metu.edu.tr/faq/how-can-i-transfer-files-and-folders-between-my-metu-user-account-and-my-computer-securely

---

## Entry 2630

Question: How can I find out about the final status of the disk space and my quota I have used up?
Answer: 

The disk space allocated for user account owners on the central servers is designated as quota. Two different quota areas are allocated for METU users and their capacities are independent from each other. While it is possible to find about the latest state of both quotas with the Horde service, it is only possible to find out about the latest status of the file quota with terminal software like SSH and others. 
Displaying quota information with Horde Service: 
First, you must enter the Horde system by https://horde.metu.edu.tr address, then you must select the File Manager option under the left menu bar's "My Account" title. You can see both the file quota and the e-mail quota information by pressing the Check Quota button.
Due to E-mail Quota applications, when quota limits are exceded, incoming e-mails can not be delivered to the receiver and will be returned to the sender. So that, it is important to use e-mail quotas within the limits.
Displaying file quota information with Shell Client Programs (SSH etc.): 
Connect to your user account by using a terminal program like SSH and write the command 
 
quota
on the command line. Click Enter to view the status of your file quota. The following screen will be displayed: 

On this screen, you will see the following terms; 
blocks indicates the space you take up on your file quota in kilobytes, quota indicates the limit of your file quota in kilobytes, limit indicates the maximum amount that your file quota could get hold of in kilobytes, grace indicates the time that has remained from your grace period, files indicates the number of files available on your file quota. 


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-find-out-about-final-status-disk-space-and-my-quota-i-have-used

---

## Entry 2631

Question: I am over quota, what should I do?
Answer: 

The disk space allocated for user account owners on the central servers is designated as quota. Two different quota areas are allocated for METU users, one for their files and one for their e-mail. The procedures to be followed are different when file or e-mail message quotas are full.
For the e-mail messages quota:
Another quota is designated for the disk area where the user keeps the e-mail messages. When 90% of this quota is full, an alert message is sent to the user.
Due to E-mail Quota applications, when quota limits are exceded, incoming e-mails can not be delivered to the receiver and will be returned to the sender. So that, it is important to use e-mail quotas within the limits.
When the e-mail messages quota is exceeded or near the upper limit, measures such as;
deleting unnecessary and bulky e-mail messages,
keeping the e-mail message attachments on the hard disk of the computer being used
may be taken and the overload on the quota can be reduced.
For the file quota:
"quota exceeded" message tells you that, at present, you are using all of the disc space that is granted to you for the files on the server systems. Currently, the procedure allows a file quota of 100 MB to students and 250 MB to the personnel.
You can display your disk usage and file quota with command quota
If you draw near to your limit value, you may not be able to access to your account. Remember that Blocks value should not be higher than the Limit value. Otherwise you will receive "quota exceed" message.
When you exceed the quota limits, the first thing you have to do is to find out the files with the largest sizes. You should either zip them or delete the unnecessary ones. Enter the following commands,
to see the spaces used by each of your file;
ls -l
ls -l |more
to zip your files;
 gzip

to open the files that you have zipped;gunzip
To change the directory you are in, enter this command;cd <directory_name>
to delete file(s) you can refer to this page
 

Link: https://faq.cc.metu.edu.tr/faq/i-am-over-quota-what-should-i-do

---

## Entry 2632

Question: What is the size of a user account quota?
Answer: 

The disk space allocated for user account owners on the central servers is designated as quota. Two different quota areas are allocated for METU users and their capacities are independent from each other.
Depending on their status, METU users have the below indicated e-mail quota on the servers:
Students:  250 MB
METU Administrative Staff and Research Assistants:  750 MB
 METU Academic Staff :  1.5 GB
When 90% of this quota is full, an alert message is sent to the user.
Due to E-mail Quota applications, when quota limits are exceded, incoming e-mails can not be delivered to the receiver and will be returned to the sender. So that, it is important to use e-mail quotas within the limits.
Depending on their status, METU users have the below indicated file quota on the servers:
Students:  100 MB
METU Staff: 250 MB
Units within the EİS Project:  250 MB
Student Groups: 250 MB
Web users: 250 MB
In compulsory cases you can apply for a file or e-mail quota increase by opening a support ticket via https://itsupport.metu.edu.tr and state the type of quota you want to increase and the reason for the increase request.


Link: https://faq.cc.metu.edu.tr/faq/what-size-user-account-quota

---

## Entry 2633

Question: How can I change my password? What should I beware of in picking a new password?
Answer: 

To change the password for your user code on Central Servers:
 From the User Account Management Page:
Sign in to User Account Management web page with your user code and password from the address belowhttps://useraccount.metu.edu.tr Then click Change Password.
 Users must create their passwords according to the following rules:
Mandatory elements in passwords are:

The password must be a minimum of 10 and a maximum of 25 characters.
The password must contain at least one uppercase letter (ABCD… .Z).
The password must contain at least one lower case letter (abcd… z).
The password must contain at least one number (1234567890).
The password must contain at least one of the special characters (?*!^...%) on the Q keyboard layout.

Elements that should not be included in passwords are:

The password cannot contain a space character.
The password cannot contain 1900s or 2000s. (1978, 1999, 2001, etc.)
The password cannot contain consecutive numbers of 4 or more characters. (1234, 2345, 5678, etc.)
The password cannot contain Turkish-specific characters. (ç, ğ, İ, ö, ş, ü…)
The password cannot contain non-ASCII characters. (ä, é, Ý, Ð, Π etc.)
The password cannot contain an easily predictable word or dictionary word, all uppercase or lowercase.
The new password cannot be the same as the last 5 passwords, if any.
Sample Passwords:
Polutk836*
Dem70:ka2b
A2K/mReD48cZ!4
2F,646(wtgRdN4#kL
EO*A(/5ybh;pTq3uRw
g1>4YjT5r3jlmZjJGU4
o)5aDA-9e2xNWYz?8cyMzV1Zr
 

Link: https://faq.cc.metu.edu.tr/faq/how-can-i-change-my-password-what-should-i-beware-picking-new-password

---

## Entry 2634

Question: How can I obtain a new password?
Answer: 

If you are a newly registering student, please refer to usercode.cc.metu.edu.tr and useraccount.metu.edu.tr
If you are a special student, you may apply at room B-14 in the  Computer Center with your temporary ID card and sign in to get your new password.
If you are faculty or admin staff, you should first get a UserCode Application Form from your unit or departmental computer coordinator and fill it out. After getting the approval of the computer coordinator, you can apply, with your personnel ID, to room B-14 in the Computer Center and get your new password.


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-obtain-new-password

---

## Entry 2635

Question: I forgot my METU user code password. Where can I apply?
Answer: 

You can get your new password if you add an alternate e-mail adress (password recovery/reset e-mail adress) using METU User Account Management https://useraccount.metu.edu.tr/ web page. To do so, you need to have a registered recovery e-mail. 
If you have a registered e-mail address, click on "Forgot password?” link
 
After filling the form, click on the “send e-mail” link. You should click the link sent to your e-mail address to reset and activate your new password.
If you remember your password and want to register a recovery e-mail address please log on to METU User Account Management page, click "REGISTER RECOVERY E-MAIL" link to register an e-mail address (other than your @metu.edu.tr address).
  
 
If you do not have an alternate/recovery e-mail address, you can simply scan your METU ID card and your identity card (only the front side) or you can take a photo of your METU ID and identity card (only the front side) with your mobile phone if applicable (allowed file types are: pdf, png, jpeg, gif and maximum file upload size: 2MB ) and fill in IT Support Form. After sending the required information to us, the recovery address would be assigned by METU CC (if there is an e-mail address that you used while sending the information or another e-mail address that you request) and you would able to perform the password recovery operations as explained above. After this process you can easily reset or change your recovery e-mail address or password whenever necessary.


Link: https://faq.cc.metu.edu.tr/faq/i-forgot-my-password-where-can-i-apply

---

## Entry 2636

Question: Password and Recovery E-Mail Procedures for METU User Codes
Answer: 

A- To change the password of your METU user code:
Visit https://useraccount.metu.edu.tr/,
Log in with your current user code and password you are using,
Click the CHANGE PASSWORD button on the following page,
Type your new password twice in accordance with the rules in Section E below and click the CHANGE button.
After a successful change, you can use your new password in a couple of minutes.
B- To set a new password in case you forget your password OR your password has been reset:
In case you forget your password, your recovery e-mail must be registered in your user account so that you can set yourself a new password. A new password activation link will be sent to your non-METU recovery e-mail address (Gmail, etc.) upon your request. You will be expected to reset your password within 24 hours via the link in the e-mail message. If your recovery e-mail is not defined in the system or if you have forgotten your recovery e-mail, follow the steps in sections C and D below.
If your recovery e-mail is defined in the system and you know your recovery e-mail;
Enter https://useraccount.metu.edu.tr/,
Under the User Login section, click "Forgot your password?"
Click on the "SEND E-MAIL" button after entering the "username", "recovery e-mail" defined in the system, and the "image verification" characters.
Check your recovery email address inbox. A new password activation link will be sent to your address. Click on the activation link on the next page.
When you click the activation link, you will be directed to the page where you can create a new password. When you create a new password in accordance with the criteria specified in section E, you will see the message that your password has been successfully changed.
After a successful change, you can use your new password in a couple of minutes.
If the recovery e-mail address you typed is not the same as the e-mail address registered in the system, you will have a warning message “Recovery E-Mail mismatch. Please make sure you enter your registered recovery e-mail."  If you do not remember your recovery e-mail, you cannot set your recovery e-mail yourself as you also do not know your password. In this case, please fill out the form at https://itsupport.metu.edu.tr/ and ask for your recovery e-mail to be registered in the system. You will be notified of your recovery e-mail address registered in the system. With the e-mail recovery address you learned, you can set yourself a new password by following the steps above.
C- To define a recovery e-mail:
Visit https://useraccount.metu.edu.tr/,
Login with the current user code-password you are using,
Click SET RECOVERY EMAIL button on the following page,
Write your recovery email and click the UPDATE button.
D- If you cannot define a recovery e-mail yourself because you forgot your password:
First of all, have your METU ID and T.C. ID cards ready. Scan the front of your identity card (both together) in a scanner or take a picture from your mobile phone. (In order to upload files, the photo must be one of the pdf, png, jpeg, gif file types and has a maximum size of 2mb),
Enter the address https://itsupport.metu.edu.tr/.
Click the "Fill out the Information Support Form" button on the next page.
Fill in the requested information on the screen that appears.
Click the "Upload File" button under the same screen. If the button is in the "Off" position, click on the text Off and turn it to the "On" position. And upload your ID cards.
After entering the verification code at the bottom of the page, click the "Submit" button.
After we receive your request, your recovery e-mail address will be registered by us. (the address you send e-mail from or an address you request if you have specified)
E- Our users should create their passwords according to the rules on the following page:

How can I change my password? What should I beware of in picking a new password?


Link: https://faq.cc.metu.edu.tr/faq/password-and-recovery-e-mail-procedures-metu-user-codes

---

## Entry 2637

Question: What is a recovery e-mail address?
Answer: 

In case you forget your METU password, you can get a new one if you have an alternate e-mail address (password recovery e-mail address) registered in METU User Account Management https://useraccount.metu.edu.tr/ web page.
To register a recovery e-mail address, after you log on to METU User Account Management page with your current username and password, please click "REGISTER RECOVERY E-MAIL" link in the above menu to register an e-mail address. In the box provided, you can type an alternate e-mail address. After you register a recovery e-mail address, you will receive an e-mail that you have an updated recovery e-mail address.
 
Once you have a registered e-mail address, you can get a new password by clicking on "Forgotten your password?” link and following the instructions.


Link: https://faq.cc.metu.edu.tr/recovery_email_addresses

---

## Entry 2638

Question: ABBYY
Answer: 


— ABBYY FINEREADER 10 —
ABBYY FineReader is an optical character recognition (OCR) application. Abbyy FineReader software converts the printed documents into digital formats after scanning and converts files in formats like jpeg, bmp, and pdf into editable text document files (like .txt or .docx).
You can perform the installation and activation of the software by following the steps below.
INSTALLATION
ACTIVATION


[1] Note: The software, which also supports Turkish characters and a dictionary, can only work in the METU campus with simultaneous licensing over the network, in accordance with the license agreements made, and is only open to the use of METU personnel.


STEP-1 <<<INSTALLATION>>>
Start the installation by running the “Setup” file.

STEP-2
Click on the "OK" button to proceed.


STEP-3

Select the “Typical” option and click on the "Next" button to proceed.


STEP-4

Click on the "Install" button to proceed.

STEP-5


Click on the “Finish” button to complete the installation process.

STEP-6 <<<ACTIVATION>>>

For licensing, right-click the "change_hosts_license" file in the "hosts_batch" folder in the "metuabbyy10" iso file and run it as an administrator with the "Run as administrator" option. After this step, you can start using the software. 



Contact us: https://itsupport.metu.edu.tr/




Link: https://faq.cc.metu.edu.tr/Abby

---

## Entry 2639

Question: ACCESS TO ADOBE SOFTWARE
Answer: 


— ADOBE CREATIVE CLOUD // ACROBAT PRO —
In order to access the limited number of Adobe Creative Cloud and Adobe Acrobat Pro software licenses, ODTU e-mail addresses and the Adobe account access password associated with these addresses can be used.
Our users, who obtain the e-mail address and Adobe account access password information authorized to access Adobe software, can use the software by following the steps below.


[1] Note: Adobe software is available to technical staff only! (Adobe licenses used by technical units and provided in limited quantities are not available to staff or students.)
[2] Note: The e-mail address and Adobe account password defined for accessing Adobe software made available should not be shared with third parties for both security and common use!
[3] Note: You can use the Adobe Acrobat extension for free by adding it to your browser to view, convert, compress or sign PDFs. Click here: https://faq.cc.metu.edu.tr/adobe-acrobat-browser-extension for detailed information.



STEP-1

Go to https://www.adobe.com/ and click the “Login” button on the top right of the page.


STEP-2

Continue by logging in with your e-mail address and Adobe account access password on the opened page.

STEP-3


To log in, select the “ODTU Bilgi Islem” profile.


STEP-4

Click on the “Creative Cloud” icon among the products listed under the application menu at the top right of the page.

STEP-5


Proceed by clicking the "Download" button under the Creative Cloud area in the window that appears.


STEP-6

Find and run the installer in the downloads section of your browser or in the location where you saved your downloaded files on your computer.


STEP-7

Click the “Continue” button to start the installation. When the installation starts, you will be directed to a web page for user login. Log in with your e-mail address and Adobe account access password on this page.

STEP-8


If the user login is successful, a warning message will appear on the screen as follows. After the user login is complete, the installation continues and completes.

STEP-9


After the installation is completed, you can download and start using the software you want to use.


STEP-10
Since only one person can use the software at the same time, it is absolutely necessary to sign out after using the software. Otherwise, other users cannot access the software.



Contact us: https://itsupport.metu.edu.tr/





Link: https://faq.cc.metu.edu.tr/faq/access-adobe-software

---

## Entry 2640

Question: ADOBE ACROBAT BROWSER EXTENSION
Answer: 

— ADOBE ACROBAT CHROME EXTENSION —
Edit PDFs right in your Google Chrome browser with Adobe’s Acrobat extension.
You can install and enable the extension by following the steps below.
INSTALLATION
ENABLE


STEP-1 <<<INSTALL EXTENSION>>>
You can add the extension to your browser by going to the Google Chrome Store via the link below.
https://chrome.google.com/webstore/detail/adobe-acrobat/efaidnbmnnnibpcajpcglclefindmkaj
STEP-2 <<<ENABLE EXTENSION>>>
Open Google Chrome and click the Chrome menu icon in the upper-right corner of the Chrome toolbar. Then choose "More Tools > Extensions".

STEP-3
Click the toggle button to turn on the Adobe Acrobat extension.

STEP-4
Open a web page in a new Chrome tab or refresh any other existing tab. The extension is enabled once the web page is completely downloaded. After this step, the extension is ready to use. Click the Adobe Acrobat icon to see the options.



Contact us: https://itsupport.metu.edu.tr/







Link: https://faq.cc.metu.edu.tr/adobe-acrobat-browser-extension

---

## Entry 2641

Question: ANSYS
Answer: 


— ANSYS 2024 R1 —
ANSYS is a finite element analysis software that especially can be used in engineering applications.
You can perform the installation and activation of the software by following the steps below.
INSTALLATION
ACTIVATION
LICENSE SERVER ACCESS SETTINGS & ACTIVATION
ERROR MESSAGES & SUGGESTED SOLUTIONS


[1] Note: Our students can access the student edition of ANSYS software at https://www.ansys.com/academic/students
[2] Note: For ANSYS software content and modules, please visit https://www.ansys.com/academic/educators/academic-product-portfolio
[3] Note: Our usersusing versions before ANSYS 2020 R1 need to make the settings on this link in order to use the Electronics module. It is recommended that our users use the latest version of the software under all circumstances.



STEP-1 <<<INSTALLATION>>>

Click on the "Install Ansys Products" button to proceed.

STEP-2


Select the “I agree ...” option and click on the "Next" button to proceed.


STEP-3

Click on the "Next" button to proceed.


 

STEP-4


Click on the "Next" button to proceed.

STEP-5


Select the “No. Skip configuration. I will configure later” option and click on the "Next" button to proceed.

STEP-6


Click on the "Next" button to proceed.

STEP-7


When prompted, mount the "ANSYS2024R1_WINX64_DISK2" iso installation file numbered "#2" and select it by clicking the "Browse" button. Then proceed by clicking the “OK” button.

STEP-8


When prompted, mount the "ANSYS2024R1_WINX64_DISK3" iso installation file numbered "#3" and select it by clicking the "Browse" button. Then proceed by clicking the “OK” button.

STEP-9


Click on the "Next" button to proceed.

STEP-10


Click on the "Exit" button to complete the installation process.




LICENSE SERVER ACCESS SETTINGS & ACTIVATION

STEP-11

To enter activation information, run the “Ansys Licensing Settings 2024 R1” tool and make the relevant definitions according to the information in the screenshots below.

>> ANSYS TEACHING



>> ANSYS RESEARCH 


To set the license server access settings, save the “ansyslmd.ini” file in the "C:\Program Files\ANSYS Inc\Shared Files\Licensing" directory as follows (this file may be in a different directory depending on the directory you installed the software in) and then close and reopen the ANSYS software.
>> ANSYS TEACHING
SERVER=1056@license.cc.metu.edu.tr
ANSYSLI_SERVERS=2325@license.cc.metu.edu.tr
>> ANSYS RESEARCH
SERVER=1055@license2.cc.metu.edu.tr
ANSYSLI_SERVERS=2325@license2.cc.metu.edu.tr


ERROR MESSAGES & SUGGESTED SOLUTIONS
ERROR CODE
ISSUE
TROUBLESHOOTING

N/A –
Not Applicable

Not enough ANSYS HPC licenses
The Ansys HPC (related to core usage in analysis) campus license includes a common HPC pool. Therefore, users on the campus using Ansys CFD, Mechanical, and Electronics software use the same common HPC repository. As there may be more Ansys CFD and Mechanical users in the campus license, they may have used cores from the common HPC repository. Thus, users using Ansys Electronics software may have fewer cores left, as the number of cores in the common HPC pool will vary according to the use of other users. Therefore, the number of HPC core usage, which varies in the number of users using HPC cores, maybe due to this reason.

N/A –
Not Applicable

Connection timed out while reading data
To solve the Ansys Workbench "Connection timed out while reading data" error, you need to add "cc.metu.edu.tr" as DNS suffix in your network adapter settings for domain name resolution. You can follow the similar steps in the link below. URL > > https://answers.uillinois.edu/illinois/114224


Contact us: https://itsupport.metu.edu.tr/




Link: https://faq.cc.metu.edu.tr/ansys

---

## Entry 2642

Question: ARCGIS DESKTOP
Answer: 


— ARCGIS DESKTOP 10.8.2 —
ArcGIS Desktop is a complete desktop GIS software suite that allows you to create maps, perform spatial analysis and manage data.
You can perform the installation and activation of the software by following the steps below.
INSTALLATION
ACTIVATION


[1] Note: ArcGIS Desktop software is available to both staff and students under the license agreement.


STEP-1 <<<INSTALLATION>>>
For installation, click the “ArcGIS_Desktop_1082_180378.exe” installation file in the iso file and run it, then click the “Next” button to proceed.


STEP-2

Check the "I accept the master agreement" option. Then, proceed by clicking the “Next” button.
 
STEP-3


Proceed by clicking the “Next” button.


STEP-4

Proceed by clicking the “Next” button.


STEP-5

Proceed by clicking the “Next” button.


STEP-6

Proceed by clicking the “Install” button.


STEP-7

Click on the “Finish” button to complete the installation process.


STEP-8 <<<ACTIVATION>>>

After the installation is finished, the “ArcGIS Administrator Wizard” window will open. Check the “Advanced (ArcInfo) Concurrent Use” option under the ArcGIS Desktop heading to select the software to use. Then, for the activation process, type "arcgis.cc.metu.edu.tr" as the license server name in the field under License Manager and then click the "OK" button.


STEP-9
In this window, you can access information about the software you have installed and the current license availability. You can close the window by clicking the “OK” button and start using the software.



Contact us: https://itsupport.metu.edu.tr/







Link: https://faq.cc.metu.edu.tr/arcgis-desktop

---

## Entry 2643

Question: ARCGIS ONLINE
Answer: 

— ARCGIS ONLINE —
ARCGIS ONLINE is a collaborative web GIS that allows you to use, create, and share maps, scenes, apps, layers, analytics, and data. You get access to content in ArcGIS Living Atlas of the World, ArcGIS apps, and cloud infrastructure, where you can add items; publish web layers; and create maps, apps, and scenes. ArcGIS Online can be used as an integral part of the ArcGIS system, extending the capabilities of ArcGIS Pro.
What you can do with ArcGIS Online:
Make maps
Share maps and apps
Collaborate
Analyze data
Work with your data


Account - How do I sign up?
Users are not authorized to create an account, as ArcGIS Online is offered as part of existing ArcGIS licensed software. However, users who request to use ArcGIS Online can submit their requests via the IT Support web page below. After your account is created, click on the link in the email you will receive within 14 days and create your account password. You can then log in to ArcGIS Online and access the provided resources.
IT Support: https://bilisimdestek.metu.edu.tr/
Account - How do I access?
To access ArcGIS Online, click on the link below and log in by entering your username and password on the page that opens.
ArcGIS Online: https://www.arcgis.com/home/signin.html


Contact us: https://itsupport.metu.edu.tr/







Link: https://faq.cc.metu.edu.tr/arcgis-online

---

## Entry 2644

Question: ARCGIS PRO
Answer: 


— ARCGIS PRO 3.2 —
ArcGIS Pro is a suite of programs that brings together the necessary features for Geographic Information Systems (GIS), developed by ESRI. It is known as the new version of ArcGIS for Desktop.
You can perform the installation and activation of the software by following the steps below.
INSTALLATION
ACTIVATION


[1] Note: ArcGIS Pro software is available to both staff and students under the license agreement.


STEP-1 <<<INSTALLATION>>>
For installation, click the “ArcGIS Pro_32_188049.exe” installation file in the iso file and run it, then click the “Next” button to proceed.


STEP-2

Proceed by clicking the “Next” button.


STEP-3

Check the "I accept the master agreement" option. Then, proceed by clicking the “Next” button.


STEP-4

Proceed by clicking the “Next” button.

STEP-5


Proceed by clicking the “Install” button.

STEP-6


Click on the “Finish” button to complete the installation process.

STEP-7 <<<ACTIVATION>>>


ArcGIS Pro will start after the installation is complete. To set the licensing options, click on the "Settings" button from the menu on the left.

STEP-8


Click on the "Configure your licensing options" button in the "Licensing" option from the menu on the left.


STEP-9
Select the "Concurrent Use License" option in the window that opens and type "arcgis.cc.metu.edu.tr" into the relevant field as "License Manager". You can choose which features you want to use from the active areas and start using the software.



Contact us: https://itsupport.metu.edu.tr/




Link: https://faq.cc.metu.edu.tr/arcgis-pro

---

## Entry 2645

Question: AUTODESK 3DS MAX DESIGN
Answer: 

3ds Max Installation
1.Step: You should choose “Install Products” on the screen.
 
2.Step: You must install components. Therefore, all components must be checked. You should click Next button to continue.
  
3.Step: Components installing. This will take time. Please wait.
 
4.Step: Firstly, you have to accept license agreement to install. Then, you should click Next button.
 
5.Step: You should choose “I have my product information” option. Then, you should go to:  https://software.cc.metu.edu.tr and find serial.txt where software.iso was downloaded. You should enter serial number with the help of txt file. You should just click Next button to continue.
 
6. Step: You must click Configure button on this screen.
 
7.Step: You should choose “Network License” option. And name of the server must be: “autodesk.cc.metu.edu.tr”. Then, you should click Configuration Complete button to activate product.
 
8. Step: You should click Install button to install the product. Product will be installed.
 
You can ask related questions via https://itsupport.metu.edu.tr/


Link: https://faq.cc.metu.edu.tr/autodesk-3ds-max-design

---

## Entry 2646

Question: AUTODESK AUTOCAD
Answer: 

Note For Students: You can download Student Edition at https://www.autodesk.com/education/edu-software/overview?sorting=feature... 
 
Installation
 
 
Installation
Autocad software can be downloaded from https://software.cc.metu.edu.tr/.
1.Step

2.Step

3.Step

4.Step: Serial Number and Product Key can be found at "https://software.cc.metu.edu.tr".

5.Step: Choose "Configure" and configure installation settings.

6.Step: "autodesk.cc.metu.edu.tr" should be given as license server.

7.Step Proceed by clicking "Yes" on the warning screen.

8.Step

9.Step

10.Step

11.Step

NOTE: After the installation process is completed, download and install the two updates from the software.cc.metu.edu.tr address in order! An error message will appear on the screen while trying to install updates. Follow the steps below to bypass this error while installing. Follow the steps below for two updates.
Step-1 When you start to install the updates, close the warning below and proceed to the second step.

Step-2 Follow the "Task Manager > File > Run new task" path to proceed.

Step-3 Click Browse > Select the update from the location where you downloaded it to your computer > Tick the box "Create this task with administrator privileges" > Click the "OK" button to complete the installation process.

 
Related questions and problems can be sent via https://itsupport.metu.edu.tr/


Link: https://faq.cc.metu.edu.tr/autodesk-autocad

---

## Entry 2647

Question: AUTODESK AUTOCAD CIVIL 3D
Answer: 

It is a building information modeling(BIM) for design, analysis and simulation for civil engineers. Autodesk Civil 3D can be downloaded from "https://software.cc.metu.edu.tr".
 
Installation
 
Installation:
1. Step:

2. Step:

3. Step:

4. Step: Serial Number and Product Key can be found at "https://software.cc.metu.edu.tr".

5. Step: Choose "Configure" and configure installation settings.

6. Step: "autodesk.cc.metu.edu.tr" should be given as license server.

7. Step:

8. Step:

9. Step:

10. Step:

11. Step:

12. Step:

13. Step:

14. Step:

15. Step:

 
 
Related questions and problems can be sent via https://itsupport.metu.edu.tr/


Link: https://faq.cc.metu.edu.tr/autodesk-autocad-civil-3D

---

## Entry 2648

Question: AUTODESK AUTOCAD INVENTOR
Answer: 

Autodesk Inventor, is a computer-aided design application for creating 3D digital prototypes used in the design, visualization and simulation of products. Autodesk Inventor can be downloaded from "https://software.cc.metu.edu.tr".
 
Installation
 
Installation
1. Step:

2. Step:

 
3. Step:

4. Step:

5. Step: Serial Number and Product Key can be found at "https://software.cc.metu.edu.tr".

6. Step:

7. Step: Choose "Configure" and configure installation settings.

8. Step: "autodesk.cc.metu.edu.tr" should be given as license server.

9. Step:

10. Step:

11. Step:

12. Step:

13. Step:

14. Step:

15. Step:

 
Related questions and problems can be sent via https://itsupport.metu.edu.tr/


Link: https://faq.cc.metu.edu.tr/autodesk-autocad-inventor

---

## Entry 2649

Question: AUTODESK ECOTECT ANALYSIS
Answer: 

It is an environmental analysis tool that allows designers to simulate building performance from the earliest stages of conceptual design. Autodesk Ecotect can be downloaded from "https://software.cc.metu.edu.tr".
Installation
 
Installation:
1. Step:

2. Step:

3. Step:

4. Step: Serial Number and Product Key can be found at "https://software.cc.metu.edu.tr".

5. Step:

6. Step:

7. Step:

8. Step:

9. Step:

10. Step: "autodesk.cc.metu.edu.tr" should be given as license server.

11. Step:

12. Step:

 
 
Related questions and problems can be sent via https://itsupport.metu.edu.tr/


Link: https://faq.cc.metu.edu.tr/autodesk-ecotect-analysis

---

## Entry 2650

Question: AUTODESK REVIT ARCHITECTURE
Answer: 

It is building information modeling software for architects, structural engineers, MEP engineers, designers and contractors. Autodesk Revit can be downloaded from "https://software.cc.metu.edu.tr".
 
Installation
 
Installation:
1. Step:

2. Step:

3. Step:

4. Step: Serial Number and Product Key can be found at "https://software.cc.metu.edu.tr".

5. Step:

6. Step: "autodesk.cc.metu.edu.tr" should be given as license server.

7. Step:

8. Step:

9. Step:

10. Step:

11. Step:

12. Step:

13. Step:

14. Step:

15. Step:

 
 
Related questions and problems can be sent via https://itsupport.metu.edu.tr/


Link: https://faq.cc.metu.edu.tr/autodesk-revit-architecture

---

## Entry 2651

Question: COMSOL
Answer: 


— COMSOL 6.0 —
COMSOL is a multiphysics and finite element analysis (FEA) software. Our Comsol Academic license includes the following modules.
COMSOL Multiphysics
-  CFD Module
-  Chemical Reaction Engineering Module
-  Heat Transfer Module
-  LiveLink for MATLAB
You can perform the installation and activation of the software by following the steps below.
INSTALLATION
ACTIVATION


[1] Note for students: Comsol software cannot be offered to students due to license agreement. Students can use the software in PC labs.


STEP-1 <<<INSTALLATION>>>
Select the language option you want for the installation and proceed by clicking the “Next” button. (In this installation, “English” will be selected as the default language.)

STEP-2


Proceed by clicking the “New COMSOL 6.0 Installation” button.
 
STEP-3 <<<ACTIVATION>>>


At this step, you must first accept the terms of the license agreement. Select the field next to the license format title as “<port number>@<host name>”. Type “1718” in the port number field and “comsol.cc.metu.edu.tr” in the hostname field. Then, proceed by clicking the “Next” button.

STEP-4


Proceed by clicking the “Next” button.

STEP-5


Proceed by clicking the “Next” button.

STEP-6


Proceed by clicking the “Next” button.

STEP-7


Proceed by clicking the “Install” button. 

STEP-8

Click the “Close” button to finish the installation process.



Contact us: https://itsupport.metu.edu.tr/




Link: https://faq.cc.metu.edu.tr/comsol

---

## Entry 2652

Question: DEMOCREATOR
Answer: 


— DEMOCREATOR —
Democreator is a screen recorder and video editing tool that can be used to make tutorial videos, demo videos, presentation recordings, game vlogs, and other information-sharing videos.
A certain number of Democreator software licenses have been provided for our university. For those who report a need from our academic departments and institutes listed on the page below, authorization has been made to the e-mail addresses sent by the relevant computer coordinators on behalf of each department/institute.
URL>> https://www.metu.edu.tr/faculties-institutes-schools
In order to access the Democreator software license, the e-mail addresses notified for our departments and institutes and the access password to be created in relation to these addresses will be used, and only one person within the department/institute can access the software at a time. Our faculty members and staff who need to use the software within the department/institute can contact the relevant computer coordinators and obtain the necessary information for access.


[1] Note: Democreator software is available to staff only.
[2] Note: The e-mail address and access password defined for access to the Democreator software made available to your department/institute should not be shared with third parties for both security and common use.
[3] Note: The name and address of the manufacturer of the Democreator software, Wondershare, are displayed on the sender line of the automatic messages sent to the department/institute e-mail address. Therefore, the messages received in this way should not be perceived as spam.
Software Website: https://democreator.wondershare.com/
Download link for Windows: https://download.wondershare.com/democreator_full7743.exe
Download link for macOS: https://download.wondershare.com/democreator-mac_full7744.zip



PART-1

Our users who have obtained the e-mail address and access password information authorized to access the Democreator software can follow the steps below to use the software.
STEP-1 
Download and install the suitable version of Democreator software for your operating system from the links in the notes section.
STEP-2 
After the installation is completed and the program is opened, in order to access all the features of the software, sign-in must be made using the e-mail address and password information obtained from the relevant computer coordinator. The software can also be used with limited features if the program is not logged in after the program is installed.
STEP-3 
Since the software can be used by only one person at the same time with all its features, it is absolutely necessary to sign out after the software is used; otherwise, other users cannot use the software in full functionality.






PART-2
The computer coordinators responsible for the department/institute where the Democreator software will be used can follow the steps below to create an access password to the software.
STEP-1 
Download and install the suitable version of Democreator software for your operating system from the links in the notes section.
STEP-2 
After the installation is completed and the program is opened, the program is entered with the e-mail address specified for the department/institute and a password can be created with the code to be sent to the relevant e-mail address by clicking the "Forget your password" link.
 






Contact us: https://itsupport.metu.edu.tr/




Link: https://faq.cc.metu.edu.tr/faq/democreator

---

## Entry 2653

Question: GAUSSIAN
Answer: 

— GAUSSIAN 09 —
GAUSSIAN 09 is the up-to-date version of the software and is licensed for campus use. Gaussian is a series of electronic structure programs that are designed to model a broad range of molecular systems under a variety of conditions. Gaussian performs its computations starting from the basic laws of quantum mechanics.
Gaussian is used by chemists, physicists, and engineers for research in established and emerging areas of chemical interest, studying molecules and reactions of definite or potential interest, including both stable species and compounds that are difficult or impossible to observe experimentally: short-lived intermediates, transition structures, etc.


[1] Note: Gaussian 09 can be run on Linux platforms (on Intel EM64T veya Intel Itanium2 IA64  architecture) and in a parallel environment (PC Clusters) with these processors.


ⵐ Gaussian 09 can be used in a parallel environment, at the PC Cluster at METU-CC, to benefit from high-performance computing capabilities.
ⵐ The PC cluster is administered by ULAKBIM High Performance and Grid Computing Center (TR-Grid). To use the software on TR-Grid a membership is required.
ⵐ For more information see http://www.truba.gov.tr/ and send an e-mail to the grid-teknik (at) ulakbim.gov.tr to become a grid member.
USEFUL LINKS
https://docs.truba.gov.tr/TRUBA/kullanici-el-kitabi/arf/uygulama-kilavuzlari/Gaussian/index.html


Contact us: https://itsupport.metu.edu.tr/




Link: https://faq.cc.metu.edu.tr/gaussian

---

## Entry 2654

Question: GRADESCOPE
Answer: 


— GRADESCOPE —
Gradescope offers online and AI-assisted grading tools for higher education. The grading software offers tools for grading written exams, homework assignments, and auto-grading submitted code. Gradescope helps instructors seamlessly administer and grade all of their assessments, whether online or in-class. Gradescope supports variable-length assignments (problem sets & projects) as well as fixed-template assignments (worksheets, quizzes, bubble sheets, and exams).



Account - How do I access?
To create your account, please follow the steps below:
Go to https://www.gradescope.com/
Click the “Sign Up” button and sign up as an “Instructor” or “Student”
Check your inbox for an email from Gradescope
Click on the “set your password” link and create your password
You can access your account now.
Gradescope is also integrated with ODTÜClass. From ODTÜClass, you can add an Gradescope activity and use.
Resources & Links
Please refer to below articles and short videos for detailed help documents/instructions related to Gradescope.
Get Started Page - A series of short how-to videos
Help Center - Written help documentation and FAQ articles available in searchable help center
Remote Assessment FAQ Guide - Guide and answers to commonly asked questions for delivering assessments remotely
Recorded Gradescope Workshop - A recording of a previous "Get Started with Gradescope for Remote Assessment" with chapters to easily navigate
Monthly Open Workshops - Anyone can sign up for our Get Started Workshop hosted every Wednesday at 3pm BST.
User Experience Videos - A series of instructors sharing their experience using Gradescope
Student Walkthrough of Gradescope - 15-minute walkthrough of the student experience with chapters for easily navigating
Bubble sheet assignments - Guidance on how to use multiple choice assignments
Basics with Bubble sheet assignments

[1] Note: For more help with Gradescope, please email vendor support at help@gradescope.com
[2] Note: From the Language drop-down menu, you can select your preferred language as Turkish. (https://www.gradescope.com/account/edit)
[3] Note: There is no "similarity check" for an essay task uploaded on Gradescope. In order to get a similarity report, our instructors can either use their account on turnitin.com or they must create a Turnitin assignment on Moodle by using the Moodle-Turnitin integration.


Contact us: https://itsupport.metu.edu.tr/





Link: https://faq.cc.metu.edu.tr/gradescope

---

## Entry 2655

Question: How to install the software using ISO (CD/DVD images) files?
Answer: 

You can download the licensed installation files on https://software.cc.metu.edu.tr within the campus borders. Some files can be accessed as CD/DVD images (ISO files) because of the technical requirements and ease of use.These image files can be written into CD/DVD (using software such as Nero, Imgburn (free)) and they can be used directly through CD/DVD.
Suggested Practical Way: 7-zip
The suggested and practical way is to download and install 1 MB sized 7-zip software from https://www.7-zip.org/ and extract the content by right clicking the downloaded ISO file. The software can be installed by running setup.exe in the newly created folder.
DAEMON TOOLS:
Daemon Tools is a software that is used to run the CD/DVD images of different folder systems (such as ISO, NRG, CUE) as virtual CD/DVD in Windows Operating Systems. In this way, it is no longer a must to write ISO files into CD/DVD or to keep the file in the same way it is extracted. This way is recommended to users who use ISO files frequently.
It is recommended to download latest version from https://www.daemon-tools.cc/eng/products/dtLite/.
Installation: Firstly, the installation file (e.g. daemon410.exe) is saved to the local machine and run. The installation may need to restart.
Configuration and Usage: after installation, you can see the icon in the notification area, right of the toolbar.. By right clicking you can specify the number of devices you can use and mount images (CD/DVDs).
Figure 1:
Lastly, Mount image option can be used specify iso image file. You can use virtual CD/DVD drive from My Computer, and install related programs in the iso image. You can Unmount drive after usage.
Figure 2:



Link: https://faq.cc.metu.edu.tr/faq/how-install-software-using-iso-cddvd-images-files

---

## Entry 2656

Question: MATHCAD
Answer: 


— MATHCAD 15 —
MATHCAD is computer software primarily intended for the verification, validation, documentation, and re-use of engineering calculations.
You can perform the installation and activation of the software by following the steps below.
INSTALLATION
ACTIVATION


[1] Note: Please note that installation is working in Windows 7 operating system, upper versions may not be appropriate for this version of Mathcad.


STEP-1 <<<INSTALLATION>>>
Proceed by clicking the “Next” button.

STEP-2


Select the "I accept" option and click the "Next" button to proceed.


STEP-3

Proceed by clicking the “Mathcad” button.


STEP-4

Select the “Use existing FLEXnet license server” option and click the “Next” button to proceed.

STEP-5


Select the “Custom” option and click the “Next” button to proceed.

STEP-6


Proceed by clicking the “Next” button.

STEP-7


Proceed by clicking the “Next” button. 

STEP-8 <<<ACTIVATION>>>

Proceed by clicking the “Add” button. 

STEP-9
Select the “Single license server” option. Type “mathcad.cc.metu.edu.tr” in the box under the hostname and “7788” in the box under the port. Then proceed by clicking the “OK” button.

STEP-10
Proceed by clicking the “Next” button.

STEP-11
Select the “Desktop” option and click the “Next” button to proceed.

STEP-12
Select the “Install Windchill Product Point Components” option and click the “Next” button to proceed.

STEP-13
Proceed by clicking the “Install” button.

STEP-14
Proceed by clicking the “OK” button.

STEP-15
Proceed by clicking the “Next” button.

STEP-16
Click the “Exit” button to finish the installation process.



Contact us: https://itsupport.metu.edu.tr/







Link: https://faq.cc.metu.edu.tr/mathcad

---

## Entry 2657

Question: MATHEMATICA
Answer: 

— MATHEMATICA 14 —
MATHEMATICA is a numerical and symbolic computation software capable of both two and three-dimensional graphics, as well as counters and density plots. 
You can perform the installation and activation of the software by following the steps below.
INSTALLATION
ACTIVATION
IMPORTANT NOTE FOR VULNERABILITY 


STEP-1 <<<INSTALLATION>>>

Proceed by clicking the “Next” button.

STEP-2


Proceed by clicking the “Next” button.


STEP-3

Proceed by clicking the “Next” button.


STEP-4

Proceed by clicking the “Next” button.

STEP-5


Proceed by clicking the “Install” button.

STEP-6


Proceed by clicking the “Finish” button.

STEP-7 <<<ACTIVATION>>>


Proceed by selecting the “Activate through a Wolfram network license server” method.



STEP-8


For the activation process, type “mathematica.cc.metu.edu.tr” in the field opposite the server name and click the “Activate” button to proceed.

STEP-9


Check the option “I accept the terms of this agreement” and click the “OK” button to proceed.

STEP-10

When the following screen appears, your installation has been completed without any problems.



IMPORTANT NOTE FOR VULNERABILITY
Recently discovered that a potential security vulnerability is found in Mathematica 11.1, 11.2, and 11.3 on Linux operating systems. Under certain circumstances, users of your system could execute arbitrary Wolfram Language code as root. Recent versions of Wolfram systems containing VernierLink were shipped with a vulnerability potentially allowing non-root users to run arbitrary commands as root. This only affects machines where the Wolfram System was installed as root. We therefore strongly recommend you apply the following steps to all Linux systems on which any of these Wolfram System versions are installed.
Resolution:
If you do not use or plan to use the VernierLink functionality in Mathematica, remove the vulnerable file:

sudo rm /etc/udev/rules.d/wolfram-vernierlink-libusb.rules 
You may be prompted to provide admin-level credentials to complete this action.
If you are connecting Mathematica to Vernier-branded external devices using VernierLink, adjust the permissions of this file:

sudo chmod 644 /etc/udev/rules.d/wolfram-vernierlink-libusb.rules 
You may be prompted to provide admin-level credentials to complete this action.


Contact us: https://itsupport.metu.edu.tr/




Link: https://faq.cc.metu.edu.tr/mathematica

---

## Entry 2658

Question: MATLAB
Answer: 


MATLAB ACADEMIC — TOTAL HEADCOUNT
Warning! “MATLAB Individual” for personal use and “MATLAB Concurrent” for laboratory computers on campus should be installed.

MATLAB R2022a / INDIVIDUAL
MATLAB R2022a / CONCURRENT [for lab use only]
INSTALLATION
INSTALLATION
ACTIVATION
ACTIVATION
ERROR MESSAGES & SUGGESTED SOLUTIONS
ERROR MESSAGES & SUGGESTED SOLUTIONS 
LINK THE UNIVERSITY LICENSE TO MATHWORKS ACCOUNT

Middle East Technical University provides unlimited MATLAB and Simulink products to all Students, Academics, and Researchers.
MATLAB, Simulink, and all related add-ons are available for the entire Middle East Technical University campus. Academics, researchers, and students can use all products for learning, teaching, and research. The license you have can be installed on both university-connected computers and personal computers.
About MATLAB and Simulink
MATLAB is a technical programming language and is used for algorithm development, data analysis, visualization, and numerical computation. Simulink, on the other hand, is a visual environment used for simulation, model designs, multi-domain dynamics and embedded systems. MathWorks offers special extra products for almost 100 topics such as data analysis, image processing, and artificial intelligence.
License Installation and Activation (Students, Department and Staff)
To install the software and use other resources, for example, online education and tutorial resources, you need to access the university's portal page.
If you are new to MATLAB, you can learn simple usage in 2 hours with MATLAB Onramp online course.
Need Help?
You can access the QuickStart for Campus-Wide License or MathWorks Support pages.
Getting Started: Learning about Capabilities and Using the Software
▪ Campus-Wide Online Trainings
▪ Online Teaching with MATLAB and Simulink
▪ MATLAB Central
▪ MATLAB Parallel Server
▪ Matlab Academy (Self-Paced Online Courses)
 ▪ MATLAB Campus License Getting Started Guide



— MATLAB R2022a / INDIVIDUAL —
You can perform the installation and activation of the software by following the steps below.
INSTALLATION
ACTIVATION
ERROR MESSAGES & SUGGESTED SOLUTIONS
LINK THE UNIVERSITY LICENSE TO MATHWORKS ACCOUNT
STEP-1 <<<INSTALLATION- INDIVIDUAL>>>


Go to the MATLAB Portal provided by the Middle East Technical University.
URL >> https://www.mathworks.com/academia/tah-portal/orta-dogu-teknik-universitesi-31483888.html
Click the “Sign in to get started” button under “Get MATLAB and Simulink”.

STEP-2
Type your METU username and password into the relevant fields on the screen that appears. Then proceed by clicking the "Login" button.

STEP-3
Accept the terms of use by selecting the "I accept the terms of use" option and click the "Submit" button to proceed.

STEP-4

Select the default option for the information to be provided to the service and click the "Accept" button to proceed.



STEP-5

If you have a MathWorks account, click the “Sign In” button to log in using your university email address.

If you do not have a MathWorks account, click the “Create” button using your university email address to create one.

Log into your MathWorks account associated with your university license you created. (You must log in with your e-mail with the extension "metu.edu.tr".)



STEP-6
Click the "Download Installer" button.

STEP-7
Click the “Download for Windows” button to download the current version (R2022a). (Choose a supported platform for your system!)

STEP-8
Run the installation file you downloaded and re-enter your email address and password associated with the MathWorks account on the screen that opens. Then click the "Next" button to proceed. (In the installer, select Sign in with MathWorks Account!)

STEP-9
To accept the license terms, select "Yes" and click the "Next" button to proceed.

STEP-10 <<<ACTIVATION- INDIVIDUAL>>>
Select the "Licenses" option from the "Select license" section [MATLAB (Individual) Academic-Total Headcount] and click the "Next" button to proceed.

STEP-11
Check the information shown on the screen and write your computer's Windows user name in the empty field under the "Windows User Name" heading. Then click the "Next" button to proceed.

STEP-12


Proceed by clicking the "Next" button.


STEP-13

Select the MATLAB toolbox products you want to use and click the "Next" button to proceed. (It is recommended that the MATLAB product be selected!)


STEP-14

Proceed by clicking the "Next" button.


STEP-15

Click the "Begin Install" button to start the installation.


STEP-16
Click the "Close" button to complete the installation. You can now start using the software.
 


ERROR MESSAGES & SUGGESTED SOLUTIONS
[1] In the MATLAB TAH license, our users must complete the relevant update individually via the links below so that they do not receive the warning that "your license will expire after XX days" when they open MATLAB.
URL-1>> https://www.mathworks.com/videos/update-your-campus-wide-license-1600159973683.html
URL-2>> https://www.mathworks.com/support/search.html/answers/100222-why-do-i-receive-a-message-that-matlab-will-expire-in-xx-days.html


LINK THE UNIVERSITY LICENSE TO MATHWORKS ACCOUNT
The following instructions apply to link your MathWorks Account to a valid license.
STEP-1 
Sign in to mathworks.com (use your work or school email address). 

STEP-2
Click the “Link”  button under the “Link a License”  heading. (You can also reach the same place by selecting “My Account” from the drop-down menu under your account icon in the upper right corner.)

STEP-3
The MATLAB license belonging to your university (40901578) has been linked to your MathWorks Account. You can now start using the software.






















— MATLAB R2022a / CONCURRENT —
 [for lab use only]
You can perform the installation and activation of the software by following the steps below.
INSTALLATION
ACTIVATION
ERROR MESSAGES & SUGGESTED SOLUTIONS 


[1] Note: Within the scope of the MATLAB Academic Campus License model, the MATLAB Concurrent License provided by the MathWorks company is a license type that can be used in controlled places within the campus such as computer laboratories. The intended use of this license is limited to LAB Computers. In order to define access permission to the IP addresses of the lab computers through the central license server, it is necessary to apply through IT Support.



STEP-1 <<<INSTALLATION- CONCURRENT>>>

Run the “setup” file as administrator.

STEP-2
Proceed by clicking the “I have a File Installation Key” button under the “Advanced Options” heading.

STEP-3
Select "Yes" to accept the license terms and click the "Next" button to proceed.

STEP-4 <<<ACTIVATION- CONCURRENT>>>
Enter the installation key in the "R2022a_file_installation_key.txt" file that you downloaded into the field under the "Enter File Installation Key" heading. Then click the “Next” button to proceed.

STEP-5
Click the “Browse” button and show the path of the “license.dat” file you downloaded. Then click the “Next” button to proceed.

STEP-6 
Proceed by clicking the "Next" button.
 
STEP-7
Proceed by clicking the "Next" button.

STEP-8
Proceed by clicking the "Next" button.

STEP-9
Start the installation by clicking the "Begin Install" button.

STEP-10


Click the "Close" button to complete the installation. You can now start using the software.




ERROR MESSAGES & SUGGESTED SOLUTIONS
[1] After checking that the Internet connection is available, the “network.lic” file located at "C:\Program Files\MATLAB\(VersionNo)\licenses\network.lic" should be viewed with notepad and it should be as follows.
SERVER matlab.cc.metu.edu.tr 27005 USE_SERVER
[2] During the installation, in step 7, the "License Manager" option should not be checked. If you have checked and installed it, you need to uninstall and install it correctly.


Contact us: https://itsupport.metu.edu.tr/


 


Link: https://faq.cc.metu.edu.tr/matlab

---

## Entry 2659

Question: MAXQDA
Answer: 


— MAXQDA 24 —
MAXQDA is a software program designed for computer-aided qualitative and mixed methods data, text, and multimedia analysis in academic and scientific institutions.
You can perform the installation and activation of the software by following the steps below.
INSTALLATION
ACTIVATION
ERROR MESSAGES & SUGGESTED SOLUTIONS


[1] Note: Since the central license server does not support old MAXQDA versions, the 64-bit system and 2024 version of the software must be used.
[2] Note: In order to use the software outside of the campus, it is necessary to connect to the campus network with a VPN. Detailed information on VPN can be found at https://faq.cc.metu.edu.tr/groups/vpn-service
Download link for Windows: https://www.maxqda.de/updates/24/MAXQDA24_Setup.msi
Download link for macOS: https://www.maxqda.de/updates/24/MAXQDA24.dm


STEP-1 <<<INSTALLATION>>>


Click on the "Next" button to proceed.
 
STEP-2
Click on the "Install" button to proceed.

STEP-3
Click on the "Finish" button to proceed.

STEP-4
Select the “I accept the terms in the License Agreement” option and click on the "Continue" button to proceed.

STEP-5
Click on the "Continue" button to proceed.

STEP-6 <<<ACTIVATION >>>
Click on the "Connect to your institution's network license" button to proceed.

STEP-7
Type “maxqda.cc.metu.edu.tr” into the field under the server address and “21990” (if it does not come automatically) in the field under the port, then select the “Search for licenses automatically” option and press the “Refresh” button.

STEP-8
Click on the license name listed as"METUMAXQDA" and then click the "Connect" button.

STEP-9
If the licensing process is successful, the following warning screen will appear. You can now use the software.




ERROR MESSAGES & SUGGESTED SOLUTIONS

Error Code


Description


Suggested Solution


102x3


No license with the entered license name has been found in the MAXQDA Netlic Service.


Please check the license name for typing errors.
It should be “METUMAXQDA”.


102x7


The client is currently using the license in another instance of MAXQDA. A license can only be used in one MAXQDA instance on the same device.


Use the previously opened instance of MAXQDA or close it to use the license in the new instance of MAXQDA.
Restart the application.


102x8


The requested license is not activated or invalid.


Check whether the requested license has not been activated or has expired. If necessary, remove the license from the MAXQDA Netlic Service.


102x9


The requested license does not match this version of MAXQDA.


Please check which license has been configured to be used with this version of MAXQDA.
It should be MAXQDA 2022.


102x10


The client device is not on the whitelist or cannot be added automatically and therefore does not have permission to use the license.


Check whether the name that was entered is correct.


102x11


The client device is listed on the blacklist and is therefore excluded from the use of the license.


Use VPN for out-of-campus entries.


102x12


The maximum number of simultaneously connected clients has been reached for the requested license.


A new space will be available once a currently connected client stops working with MAXQDA.


104x15


A connection to the MAXQDA Netlic Service could not be established or was disconnected.


Please check your network connection and the specified server address as well as the port.






Contact us: https://itsupport.metu.edu.tr/





Link: https://faq.cc.metu.edu.tr/maxqda

---

## Entry 2660

Question: MICROSOFT 365 
Answer: 


— MICROSOFT 365 —
Eligible staff and students can sign up for Microsoft 365 (formerly known as Office 365) for the classroom for free, including Word, Excel, PowerPoint, OneNote, and Microsoft Teams, plus additional classroom tools for the duration of their time at the university.
Microsoft 365 is licensed as part of your METU email account.
Important Note: In line with the global policy change by Microsoft, the OneDrive storage space offered to Microsoft Office 365 users within the corporate storage area will no longer be available. In this context, to prevent possible data loss, we recommend that you back up your data on OneDrive to an external storage area and free up this space until August 1, 2024.


Important Notice-3! 
If Microsoft 365 applications are to be used for the first time, you should register with the METU user account xxxxxx@metu.edu.tr via https://www.microsoft.com/en-us/education/products/office and follow the specified steps.
If you have previously registered with Microsoft 365 applications with the METU user account xxxxxx@metu.edu.tr; to download and install these applications on personal devices, you should log in to https://www.microsoft365.com/ with the METU user account xxxxxx@metu.edu.tr used during Microsoft registration and the Microsoft password created for this.
Due to the Microsoft infrastructure change announced in our university in the past months, our users who have previously created a Microsoft registration as xxxxxx@metu.edu.tr may encounter an error when logging in to Microsoft 365 applications in the newly switched infrastructure. This error is caused by old sessions opened and registered to Microsoft services that were previously installed on the computer. Our users who experience login errors can follow the steps below as recommended by Microsoft:
For Windows users:
Press windows key + R to open the Run, Type %localappdata%/Microsoft and Enter.
Delete  OneAuth  and IdentityCache folder from there.
Open credential manager and click on the click on the windows credentials.
Delete all the generic credentials related to office 365.
Open Registry editor and follow the path HKEY_CURRENT_USER\Software\Microsoft\Office<16.0>\Common\Identity.
Delete the identity folder.
Restart the computer and try to log into the apps.
For MAC users:
Delete the office suite and install it again.
If it does not work, use the following steps to delete the cache.
Method-1
Open Finder and press Shift + Command + G to open the Go to folder window.
Type      /Library/Containers//com.Microsoft.OsfWebHost/Data/  and press Go.
Select all files in this folder and delete them.
Method-2
Using terminal type the following command      rm -rf /Library/Containers/com.Microsoft.OsfWebHost/Data/*    and press enter
If the login error persists due to these steps, a support request can be made via https://bilisimdestek.metu.edu.tr/


Important Notice-2! 
Dear Members,

Recent announcements have shared that Microsoft will globally change its licensing policies, and therefore, it has become necessary to implement a two-phase adjustment in our current Microsoft software services.

In the first stage, as stated in the announcement, required members benefiting from Office 365 services to individually back up/delete all their data on OneDrive, Teams, and other Microsoft services.

The second stage, to be carried out between June 24 and July 1, 2024, involves discontinuing the Office 365 A1 Plus licenses used in our university and providing access to new licenses through a new infrastructure.

As part of the second stage, there will be planned restrictions on access to existing Microsoft services during the specified dates. Disruptions may occur when logging into Microsoft Teams, Office 365 software, and other Microsoft services. After the stage is completed on July 1, 2024, all our members will be able to access Microsoft services via their new "@metu.edu.tr" email addresses (e.g., for staff: namesurname@metu.edu.tr // for students: e123456@metu.edu.tr) and new access passwords, which they will obtain by following the "Forgot my password" steps, through the new infrastructure.

After the transition to the new infrastructure, it will not be possible to access data in the old infrastructure using the "@metu.edu.tr" Microsoft accounts and new access passwords. Members wishing to access their data in the old infrastructure will be able to log into Microsoft services with temporarily created "@metu2.metu.edu.tr" email addresses (e.g., for staff: namesurname@metu2.metu.edu.tr // for students: e123456@metu2.metu.edu.tr) and their old Microsoft account passwords. The old infrastructure accounts will remain available for a while to allow members to back up their old data.

Detailed information on the subject can be accessed at https://faq.cc.metu.edu.tr/microsoft365. Possible questions or issues can be submitted via https://bilisimdestek.metu.edu.tr/.

We present this information for your attention.

Regards,
Computer Center


Important Notice-1! 
Dear All,
Microsoft has announced that it will make global changes to its licensing policies. As part of these changes, the Office 365 A1 Plus licenses currently used at our university will be discontinued, and the 1 TB OneDrive, Exchange, and SharePoint cloud storage capacity, which is recognized on a user basis, will no longer be available.
To ensure uninterrupted access to Microsoft software for university members, it is mandatory to make adjustments in our existing Microsoft software services based on the announced changes.
In the first stage, the 1 TB OneDrive, Exchange, and SharePoint quotas recognized on a user basis in Office 365 accounts associated with our members’ @metu.edu.tr email addresses will be restricted as of June 30, 2024. Therefore, members benefiting from Office 365 services need to individually back up or delete their OneDrive, Teams accounts (including records and channels), and all data in Microsoft services by this date. Failure to take action by the specified date will make the account owner responsible for any service interruptions or data loss in Office 365 accounts. If the relevant data in Office 365 accounts continues to be stored without any backup or deletion, there is a possibility that Microsoft may delete this data, and access to it may not be possible after some time.
Details of the planned adjustments related to Microsoft software services in the second stage will be announced later.
For more detailed information on this topic, you can visithttps://faq.cc.metu.edu.tr/microsoft365 .
We sincerely appreciate your attention.
Best regards,
Computer Center 


[1] Note for eligibility: Microsoft 365 is available for free to all current students and staff. Microsoft 365 subscription will be valid throughout your time as a student or staff at METU. Once you have graduated or left the University, copy the data (emails, attachments, OneDrive, etc.) you want to save before your account is closed. Accordingly, at the time of account closure, all data and information stored in the cloud service will no longer be accessible or recoverable. Please regularly backup or sync all files to your personal computer to avoid losing files and data.
[2] Note for license activation: Activate your Microsoft 365 by signing in with your staff/student email address and password linked to your Microsoft account when prompted after opening one of the Office applications. This will ensure you get the full version of Microsoft 365 in accordance with the university's license.
[3] Note for students: When registering for the Microsoft 365 service, students must register with an e-mail address such as e123456@metu.edu.tr. Registering with aliases defined in e-mail addresses such as name.surname@metu.edu.tr is strictly prohibited in accordance with the license agreements.
[4] Microsoft Office 365 Announcement: There will be changes in Microsoft Office 365 services connected to METU e-mail accounts as of June 30, 2024. As of this date, there will be no OneDrive quota for Office 365 services. You must back up/delete all your data in OneDrive, your Teams account (including recordings and channels), and Microsoft services by the specified date. If your accounts are not brought into compliance with the new terms/conditions by this date, you will be subject to any service interruptions, data loss, etc. The user who owns the relevant e-mail is responsible for such situations. We want to remind you that the data stored in your accounts will be irreversibly lost according to the specified conditions.
[5] Note for Graduate and Retired users: Our graduate and retired users still have the opportunity to access their old data. There is no new registration option for both our graduate and retired users on the new infrastructure.


WHO IS THIS SERVICE AVAILABLE TO?

This service is available to eligible METU staff and students!
WHAT IS REQUIRED FOR THIS SERVICE?
A valid METU staff or student email address is required.
HOW TO SIGN UP? // Get started with Microsoft 365!
You can sign up by following the steps below.
1 – Go to https://www.microsoft.com/en-us/education/products/office
2 – Enter your staff or student email address (enter your username as e123456@metul.edu.tr) and register.
HOW TO LOGIN? // Get access to Microsoft 365 Apps!
To download and install Microsoft 365 apps on your personal devices, please log in to the link below with your METU email address and password linked to your Microsoft account.
https://www.microsoft365.com/
USEFUL LINKS
Install Microsoft 365 Office 
Activate Microsoft 365 Office 
Uninstall Office from a PC
Uninstall Office for Mac 
Microsoft 365 Training Center 
Microsoft 365 help & learning 
Microsoft 365 Quick Starts 
Download files from OneDrive to your device 
Delete files or folders in OneDrive 
Office 365 A1 Plus for education will retire on August 1, 2024 


Contact us: https://itsupport.metu.edu.tr/







Link: https://faq.cc.metu.edu.tr/microsoft365

---

## Entry 2661

Question: MICROSOFT EDITOR
Answer: 


— MICROSOFT EDITOR: SPELLING & GRAMMAR CHECKER —
Microsoft Editor checks grammar and more in documents, mail, and the web. The Editor underlines the issues it finds. Select the underlined word or phrase to accept or ignore the suggestion.
Sign in with your Microsoft Office 365 account to get spelling, and grammar checking and get refinements beyond the basics.


[1] Note for staff & students: In order to use Microsoft Editor, follow the instructions on this page and register for Office 365 service with your metu.edu.tr e-mail address. After this process, you can access and use the related software.
[2] Note for windows users: Microsoft Editor is available in Word for Microsoft Office 365 for Windows.
[3] Note for mac users: Microsoft Editor is available in Word for Microsoft Office 365 for Mac.
[4] Note: Look for Editor on the Home tab in Microsoft Word.



Microsoft Editor for the Office 365 apps
Microsoft Office 365 subscribers get premium Editor features in Word, Outlook.com, and Outlook for the web. The Editor offers advanced grammar and style refinements like clarity, conciseness, formality, vocabulary suggestions, and more.
Microsoft Editor for the Web [Browser Extension]
You can check grammar and spelling with the Microsoft Editor browser extension. The Editor runs as an extension on Edge or Chrome. 
Get it from your browser's app store:
URL >> Edge
URL >> Chrome
Microsoft Editor Tutorial
In this step-by-step tutorial, you can learn how to use Microsoft Editor.
URL >> How to use Microsoft Editor 


Contact us: https://itsupport.metu.edu.tr/




Link: https://faq.cc.metu.edu.tr/microsoft-editor

---

## Entry 2662

Question: MICROSOFT OFFICE
Answer: 


— MICROSOFT OFFICE 2021 —
You can perform the installation and activation of the software by following the steps below.
INSTALLATION
ACTIVATION


[1] Note for staff: Microsoft Office programs are available to staff only.
[2] Note for students: In order to use Microsoft Office programs, follow the instructions on this page and register for Office 365 service with your metu.edu.tr e-mail address. After this process, you can access and use the related software.
[3] Note for windows users: Users must download the “kms_office2021_client.bat” volume license file from the licensed software web page for the “Office 2021” windows version activation process and run it with the “Run as administrator” option by right-clicking on the file. After this process, the Microsoft Office Windows version should be activated.
[4] Note for mac users: Users must download and install the “Office for Mac 2021 Serializer” volume license file from the licensed software web page for the “Office for Mac 2021” macOS version activation process. After this process, the Microsoft Office Mac version should be activated.
[5] Note for installing and using different versions of Office on the same computer: "If you have a Microsoft 365 subscription or a non-subscription version of Office Home and Business like 2021, 2019, 2016, or 2013, in most cases you cannot run these versions together on the same computer."



STEP-1 <<<INSTALLATION>>>

Click on the “install” button to start the installation. (If necessary, right click on the install file and run as administrator.)


STEP-2

After the installation starts, the following two windows will open on the screen. Do not close these windows until the installation is complete.

 
STEP-3


Click on the “Close” button to finish the installation process.


STEP-4 <<<ACTIVATION>>>

For the activation process, right-click the "kms_office2021_client.bat" file and run it with the "Run as administrator" option.

STEP-5

If you see the text “Product activation successful” in the window that appears, it means that the activation process has been completed successfully.
 


Contact us: https://itsupport.metu.edu.tr/




Link: https://faq.cc.metu.edu.tr/office

---

## Entry 2663

Question: Email address activation for newly registered students
Answer: 

Email addresses for new registered students will be activated after Add-Drop period.
 


Link: https://faq.cc.metu.edu.tr/faq/email-address-activation-newly-registered-students

---

## Entry 2664

Question: Are there any limitations for the attachments of incoming E-mail?
Answer: 

The size of the attachments of e-mail that arrives at your account registered on central e-mail server should not exceed 25 MB. When the user tries to send mail greater than 25 MB the e-mail server will reject it anyway. Her/his e-mail handling software will inform the user of the situation by an alert message.


Link: https://faq.cc.metu.edu.tr/faq/are-there-any-limitations-attachments-incoming-e-mail

---

## Entry 2665

Question: Are there any limitations for the attachments of outgoing E-mail?
Answer: 

When sending an e-mail, the maximum size of the attached files to be handled by METU central e-mail servers must not be over 25 MB. Such files should be compressed (zip) or divided (multiple file zip), and then sent.


Link: https://faq.cc.metu.edu.tr/faq/are-there-any-limitations-attachments-outgoing-e-mail

---

## Entry 2666

Question: Can I forward my e-mails that arrive at my METU user account after I graduate?
Answer: 

In the scope of the Forwarding Service, the e-mail addresses of graduated students in the e100001metu.edu.tr format are left active for a term after graduation (for Spring term graduates till the March of the next year and for Fall graduates till November of the same year) and terminated and directed to an indicated e-mail address forever, at the end of that duration .
For prospective graduate students, a warning message is sent 6 months before, stating that their account will be terminated, followed by a reminding message 1 month before the termination. The students can do the forwarding after the reminding message before the termination or whenever they want after their account is terminated.
For more information on e-mail forwarding, please visit https://faq.cc.metu.edu.tr/faq/how-can-i-use-metu-e-mail-forwarding


Link: https://faq.cc.metu.edu.tr/faq/can-i-forward-my-e-mails-arrive-my-metu-user-account-after-i-graduate

---

## Entry 2667

Question: How can I access to my e-mails located on the central e-mail server?
Answer: 

You can access your e-mail on the central server by SquirrelMail, Horde, Wapmail, Pine or using e-mail client programs (Microsoft Outlook Express, Netscape Messenger, Mozilla Thunderbird etc.) that can be loaded on your computer, or also send e-mail.


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-access-my-e-mails-located-central-e-mail-server

---

## Entry 2668

Question: How can I create a vacation message?
Answer: 

At times when you won't be able to reply e-mail messages and you may want to automatically inform the senders of the situation, it is possible to arrange a "I am on vacation" message to be sent. This can be done by Horde interface.
With the Horde e-mail interface our users can prepare a "I am on vacation" message by using "Vacation" option under the "Filters" option under the "Mail" on the top menu of Horde where they can enter the topic and the content of the message in the boxes which are provided. The announcement can later be canceled using the same menu path.

After you enter the start and end of vacation, subject and body of the email, please click "Save and Enable" to activate the vacation responder.


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-create-vacation-message

---

## Entry 2669

Question: How can I delete an OLDINBOX and similar folders?
Answer: 

If you are using Pine program, on the main menu; 
L FOLDER LIST - Select a folder to view 
Option lets you select the folders you want and see the message content. Among these are the OLDINBOX folders. You can delete the folder you choose by highlighting/selecting the folder and keying D (Delete) and then to confirm deletion keying Y (yes).

If you are using Squirrelmail, first transfer the necessary mail in the OLDINBOX directory to another directory and delete the unnecessary mail, then click on the Folders option at the top of the page and choose from the list of directories in the Delete Folder section the OLDINBOX directory you wish to delete and click on the Delete button. 
If you are using the Horde E-Mail interface, after transferring the necessary mail in the OLDINBOX directory to another directory and deleting the unnecessary mail you must click the Folders icon and tick the box next to the OLDINBOX directory and then choose the Delete menu option.
If you are an Outlook Express, Netscape Messenger or Mozilla Thunderbird user for e-mail after removing the messages to be kept to other folders, highlight the unwanted e-mails and press Delete key on your keyboard. Afterwards, select the OLDINBOX by right clicking on the folder and select Detele command in the popup menu. 
 

Link: https://faq.cc.metu.edu.tr/faq/how-can-i-delete-oldinbox-and-similar-folders

---

## Entry 2670

Question: How can I forward e-mails incoming to my METU mail account?
Answer: 

If you want to perform forwarding with the METU Horde interface, in the top menu of Horde there is a "Filters" option under the "Mail" button that can be used. Then, select Forward option to make use of this feature. Please enter the address(es) in the "Address(es) to forward to:" box (if more than one address is necessary, separate them with a comma (,). Finally click Save and Enable button.
In order to cancel forwarding, from the Filters window, click the tick icon near the Forward text (Disable Forward).
If your forwarding settings do not work the way you want after the actions you've done, please open a support ticket via https://itsupport.metu.edu.tr
With the e-mail system put into use on 27/07/2009 it is no longer possible to redirect e-mail messages by creating a .forward file on the central server systems.
The CC in no way and never intervenes with the folders that reside in the user accounts. The errors you might make during the process of redirecting could likely cause you to lose messages, so perform the procedure with care and check by trying the result.


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-forward-e-mails-incoming-my-metu-mail-account

---

## Entry 2671

Question: How can I read e-mails in other folders such as OLDINBOX, SPAMBOX etc?
Answer: 

In the following, as an example, accessing to OLDINBOX folders are defined. The other folders, such as SPAMBOX, can be accessed similarly.
"OLDINBOX.date" formatted folders, 
If you are using Pine program on the main menu;
L FOLDER LIST - Select a folder to view
option enables you to select a folder and see your messages in that folder. Among these folders are OLDINBOX.date folders. Highlight the OLDINBOX folder that you want look at and key in Enter  to see your e-mail.

If you are using Squirrelmail, first connect to your account, to access your OLDINBOX directory click on the Folders option at the top of the page, then choose the directory listed in the Unsubscribe/Subscribe section and click on the Subscribe button thus you can now access your directory.
If you are using Horde, first connect to your account then click on the Mail button then click on the Folders button and choose the OLDINBOX directory you want and look at your e-mail messages.
If you want to look at your e-mail in the OLDINBOX using Outlook Express program your protocol should be IMAP. After changing your account settings to IMAP you should set the OLDINBOX folders visible.
In order to make the OLDINBOX folders visible;
You have to follow the menu path Tools  | IMAP Folders .
On the window that opens, find the OLDINBOX folders and click the Visible option.
Clicking on the  OK  button, the OLDINBOX.date folders will be visible below the IMAP folders.

If you are using Thunderbird program to reach/read your e-mail in the OLDINBOX, your protocol setting should be IMAP. After changing your account settings to IMAP you should set the OLDINBOX folders visible.
In order to make the OLDINBOX folders visible;
You should use the menu path  File | Subscribe .
On the window that opens, find the OLDINBOX folders and tick them.
Clicking on the  OK  button, the OLDINBOX.date folders will be visible below the IMAP folders.

 


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-read-e-mails-other-folders-such-oldinbox-spambox-etc

---

## Entry 2672

Question: How can I use METU e-mail forwarding?
Answer: 

METU Alumni and former METU staff can continue to receive e-mails sent to their METU e-mail addresses by activating the e-mail forwarding to another e-mail address they have.

Users will receive reminder e-mails 1 month before their user codes are to be terminated, informing them about the user code termination and the necessary steps for e-mail forwarding. After receiving this e-mail, they can activate e-mail forwarding with the last password they use. To activate "e-mail forwarding" service, please visit METU Portal. You can also activate forwarding via https://forward.metu.edu.tr.

After the activation of e-mail forwarding, new e-mails sent to your METU e-mail address will be automatically forwarded to the e-mail address you indicated. E-mail forwarding is not valid for already received e-mails in your inbox. If you want to archive those e-mails, please visit this link. If your METU user code has been terminated in the last 4 weeks, you can apply for backup.
To activate e-mail forwarding, you need to log in with your METU user code and password. After logging in, you can type in the e-mail address you want your METU e-mail address to be redirected to, in the Forward e-mail to text box and click Update. Then, your e-mail forwarding is activated. To deactivate e-mail forwarding, please click Forwarding on or off button.

What should you do if you cannot access your usercode?

If your user code had been terminated and you do not remember your password, please send a photo of your identity card (only the front side) and indicate your student number / staff ID number and the forwarding address you prefer via the IT Support Form. (allowed file types in the form are: pdf, png, jpeg, gif and maximum file upload size: 2MB ) Then, Computer Center IT Support Team will activate your e-mail forwarding service. You will receive an automatic e-mail once your e-mail forwarding is activated.
E-mail forwarding serves only the purpose to forward the e-mails sent to your METU e-mail address to another e-mail address you specify. No e-mails can be sent via your METU e-mail address.



Link: https://faq.cc.metu.edu.tr/faq/how-can-i-use-metu-e-mail-forwarding

---

## Entry 2673

Question: How do I filter my incoming e-mails with Microsoft Outlook Express?
Answer: 

The filtering option of incoming e-mails on Outlook Express program is only available with POP3 connections. To do this; 
you should follow this path; Tools | Message Rules | Mail.
Then, in the window displayed, you should specify the rule that will govern your filtering action and click OK button.

Follow this path afterwards; Tools | Message Rules | Block Senders.
The e-mails received from the addresses you specified in here, will be directed to Trash (Trash) folder.

 


Link: https://faq.cc.metu.edu.tr/faq/how-do-i-filter-my-incoming-e-mails-microsoft-outlook-express

---

## Entry 2674

Question: How do I filter my incoming e-mails with Pine?
Answer: 

With the e-mail system put into use on 27/07/2009 it is no longer possible to filter e-mail messages by creating a .procmail file on the central server systems. Horde or Squirrelmail services or e-mail programs such as Outlook Express, Mozilla Thunderbird etc. should be used for filtering.


Link: https://faq.cc.metu.edu.tr/faq/how-do-i-filter-my-incoming-e-mails-pine

---

## Entry 2675

Question: How do I view the full header of incoming e-mail messages?
Answer: 

If you want to forward the "full header" of your message to someone else, directly route the relevant message without adding as an attachment. You can use this when communicating to the relevant system administrator to review a spam mail you have received.
Click on the links below to see how you can view the full header in commonly used email reading programs:
Horde
Gmail
Outlook
Outlook.com/Hotmail.com Web
Mozilla Thunderbird
Yahoo.com Web
Mail for Max OS X
Roundcube Webmail
Some e-mail reading applications on mobile devices may not have full header information display capability. So, it is recommended that web or desktop based e-mail applications should be used to view full header information and sent to the Information Support Team for review.
You can check the list under the "Read Email Headers" tab at http://emailheaders.net/ for email reading programs that you can not find on this page.
 
To view the full header of your incoming message using the Horde E-Mail interface, you can use the View Source link under the + sign (Other options) when viewing the message.
 
To view the full header of your incoming message using the Gmail E-mail interface, you can use the Show Original link under the down arrow mark (Other options) on the far right of the date information on the right when viewing the message. You can get more information from the help page at https://support.google.com/mail/answer/29436?hl=en.
 
To view the full header of your incoming message using the Outlook E-mail application, double-click the incoming e-mail and click Properties on the File menu. In that window , you can view the full header on Internet Header section. You can get more information from the help page at http://emailheaders.net/outlook.html.
 
To view the full header of your incoming message using the Outlook.com/Hotmail.com Web E-mail interface, you can use the View Message Source link at the bottom of the message by clicking on the down arrow on the right side of the message. You can get more information from the help page at http://emailheaders.net/hotmail.html.
 
To view the full header of your incoming message using the Mozilla Thunderbird Email application, you can select Message Source from the View menu when viewing the message. If you can not see the View menu on the screen, you can press the Alt key altogether or press Ctrl + U together to view the entire heading of your selected message. You can get more information from the help page at http://emailheaders.net/thunderbird.html.
 
To view the full header of your incoming message using the Yahoo.com Web E-mail interface, you can use the View Raw Message link at the bottom of the message by clicking the three dot (...) button next to the Spam button at the top. You can get more information from the help page at https://help.yahoo.com/kb/SLN22026.html.
 
To view the full header of your message in Mail for Mac OS X, select the Raw Source or All Headers option from the Message menu under the View menu. You can get more information from the help page at http://osxdaily.com/2016/04/06/show-long-email-header-mac-mail-osx.
Roundcube Webmail
Open the email message. While viewing the message, click MORE and then "Show Source"



Link: https://faq.cc.metu.edu.tr/faq/how-do-i-view-full-header-incoming-e-mail-messages

---

## Entry 2676

Question: I cannot send a message from my METU account to an external e-mail address which has been directed to an address in METU. Why?
Answer: 

E-mail messages sent from a usermetu.edu.tr structured e-mail address to an e-mail address with the same structure; in other words, e-mail messages with "usermetu.edu.tr" for both the "To:" and "From:" fields (the sender and the recipient are the same) are blocked unless they are sent via "mail.metu.edu.tr" server.
This procedure is applied in order to block the unwanted messages from out of campus sources, like fake and/or spam messages, to be distributed.
For this reason, when you direct the e-mail account provided by an email service provider from outside of METU to the e-mail address with the METU central user code, e-mail messages sent from an account with a METU field name will be classified as fake/spam e-mail and blocked by the central servers since it will be conveyed through a server which is out of campus.
Important: Directing from departmental e-mail accounts (e.g. xxxxx.metu.edu.tr) is not within the scope and therefore is not blocked.


Link: https://faq.cc.metu.edu.tr/faq/i-cannot-send-message-my-metu-account-external-e-mail-address-which-has-been-directed-address

---

## Entry 2677

Question: I don't receive e-mails sent to my METU e-mail address. What can be wrong?
Answer: 

If you don't receive any e-mails sent to your METU e-mail address, please check the following:
If you use METU e-mail forwarding and you restart to work or to study at METU, the e-mail forwarding stays active as long as you disable it. For more information, please visit https://faq.cc.metu.edu.tr/faq/how-can-i-use-metu-e-mail-forwarding 
If possible, please check the sender whether the e-mail returned to them. If the e-mail returns to them, the possible reasons why the e-mail could not be delivered to you will be listed in that e-mail.
 

Link: https://faq.cc.metu.edu.tr/faq/i-dont-receive-e-mails-sent-my-metu-e-mail-address-what-can-be-wrong

---

## Entry 2678

Question: If I encounter a Turkish character problem when sending and taking e-mails, what should I do? (In Turkish)
Answer: 

Sunucu sistemlerimiz e-posta alışverişinde Türkçe karakterleri desteklemektedir. Horde ve Squirrelmail arayüzlerine Türkçe olarak girildiğinde gönderilen e-postaların karakter seti ISO-8859-9, İngilizce olarak girildiğinde ise UTF-8'dir. Her iki karakter seti de Türkçe karakterleri içermektedir. UTF-8’de Türkçe dışındaki kimi dillere özel karakterler de bulunmaktadır.
Not: Horde arayüzünde e-posta gönderirken "Karakter Seti" alanındaki seçenekleri kullanarak bu ayarı değiştirmek mümkündür.
Horde ya da Squirrelmail arayüzü dışında Outlook Express, Thunderbird ya da Windows Mail benzeri herhangi bir POP3/IMAP istemcisi ile e-posta gönderiyorsanız gönderilen e-postanın karakter seti, ilgili programın kendi ayarlarına bağlı olarak belirlenir.
Giden e-postalar için karakter seti değişikliği yapmak için farklı programlarda izlenen yol aşağıdaki gibidir (aşağıda yer almayan farklı programlar için de karakter seti ayarları benzer yerlerdedir):
Outlook Express ve Windows Mail için: Tools → Options → Send → International Settings (Araçlar → Seçenekler → Gönder → Uluslararası Ayarlar)
Mozilla Thunderbird için: Tools → Options → Display → Fonts → Character Encodings (Araçlar → Seçenekler → Görünüm → Yazıtipleri → Karakter Kodlaması)
Göndereceğiniz e-postada Türkçe karakter kullanmak istiyorsanız söz konusu menülerdeki ayarları ISO-8859-9 (Türkçe ISO olarak da tanımlanır) ya da UTF-8 seçmeniz yeterlidir.
Size gelen e-postalardaki Türkçe karakterleri görmekte sorun yaşıyorsanız iki farklı durum sözkonusu olabilir.
Karşı taraf e-posta gönderirken ya da kendisine gelen e-postayı yönlerken Türkçe karakterleri desteklemeyen bir karakter seti kullanmıştır. Bu durumda gelen mesaj düzgün olarak görüntülenemez. Örneğin metinde Türkçe karakter kullanıldığı halde gönderilirken ISO-8859-1 karakter seti kullanılmış ise söz konusu karakter seti Türkçe karakterleri desteklemediği için e-postanın düzgün olarak görüntülenmesi mümkün değildir.
Gönderilen e-posta düzgün karakter seti ile gönderilmiş olmasına karşın kullandığınız programın ayarları farklı olabilir. Bu durumda kullanılan programın ayarlarının değiştirilmesi mesajın düzgün şekilde okunmasını sağlayacaktır. Horde ya da Squirrelmail kullanarak e-posta okuyan kullanıcılarımızın kullandıkları tarayıcı programında, Outlook Express, Thunderbird ya da Windows Mail benzeri herhangi bir POP3/IMAP istemcisi ile e-posta gönderen kullanıcılarımızın ise ilgili programdaki karakter seti ayarlarını değiştirmeleri gerekmektedir.
Gelen e-postalar için karakter seti değişikliği yapmak için farklı programlarda izlenen yol aşağıdaki gibidir (aşağıda yer almayan farklı programlar için de karakter seti ayarları benzer yerlerdedir):
Internet Explorer, Outlook Express ve Windows Mail için: View → Encoding (Görünüm → Kodlama)
Mozilla Firefox ve Mozilla Thunderbird için: View → Character Encoding (Göster → Karakter Kodlaması)


Link: https://faq.cc.metu.edu.tr/faq/if-i-encounter-turkish-character-problem-when-sending-and-taking-e-mails-what-should-i-do

---

## Entry 2679

Question: Is there a limit of my account for the Inbox directory or the other directories I have created for the e-mail messages or the other files I would like to keep?
Answer: 

The disk space allocated for user account owners on the central servers is designated as quota. Two different quota areas are allocated for METU users and their capacities are independent from each other. The e-mail messages you may keep in the Inbox or other e-mail directories you have created are limited with the e-mail messages quota and the files in other directories to be created are limited by the file quota.


Link: https://faq.cc.metu.edu.tr/faq/there-limit-my-account-inbox-directory-or-other-directories-i-have-created-e-mail-messages-or

---

## Entry 2680

Question: What is IMAP and POP3?
Answer: 

IMAP (Internet Message Access Protocol) and POP3 (Post Office Protocol - Version 3) are e-mail reading services that has slight differences from each other. They enable you to easily access your e-mails while using e-mail reading programs such as Outlook Express or Netscape Messenger. 
Features of POP3:
E-mails are kept on the hard disc. If you want you may leave copies of e-mails on the server.
Outlook ExpressFrom Tools menu choose Accounts. From the properties of the desired account sellect Advanced tab and tick "Leave a copy of messages on the server".
Mozilla ThunderbirdFrom Tools menu choose Accounts. From Settings change Server Settings to "Leave messages on server" for desided mail account.
Netscape Messenger From Tools menu choose Mail & Newsgroups Account Settings. From Settings change Server Settings to "Leave messages on server" for desided mail account.

There is a preference for the user whether to delete the e-mails on the server or not while downloading them to the hard disc.
You may choose to keep your e-mails on the server, however, to be able to delete the e-mails on the server as you are deleting them from the hard disc, you should do the required settings.
If, on the server, you have created different folders and directories to separate the e-mails, these directories will not be displayed since they are not available on the hard disc.
Features of IMAP:
E-mails are kept on the server.
On the server, you can access the directories you have created or the system created.

 


Link: https://faq.cc.metu.edu.tr/faq/what-imap-and-pop3

---

## Entry 2681

Question: While sending an e-mail I get the message "blocked by SpamAssasin" alert message. Why?
Answer: 

It is planed to reduce the number of "spam" e-mail messages out going from METU with the usage of a spam filter. Within the scope of such an action, when an e-mail message gets stuck in the spam filter, an alert message will be relayed to the user via the e-mail program being used.
Below is a list of alert messages depending on the e-mail software being used.
Horde Alert Message
An error occurred while sending: Failed to send data [SMTP: Invalid response code received from server (code: 550, response: 5.7.1 Blocked by SpamAssassin)]

 
 
Squirrelmail Alert Message
ERROR: Action not taken: no mail box Server replied: 550 5.7.1 Blocked by SpamAssassin

 
 
IMAP/POP3 Client Alert Message
An error occured while sending mail. The mail server responded: 5.7.1 Blocked by SpamAssassin . Please check the message and try again.



Link: https://faq.cc.metu.edu.tr/faq/while-sending-e-mail-i-get-message-blocked-spamassasin-alert-message-why

---

## Entry 2682

Question: How can I use METU E-Mail Services with Microsoft Outlook?
Answer: 

In order to read and send e-mail via Outlook in Microsoft Office package you should configure the following settings. The New Outlook App for Windows which replaces the Mail application currently does not support IMAP/POP connections. Please click here: https://support.microsoft.com/en-us/office/getting-started-with-the-new-outlook-for-windows-66b195df-08b9-48bd-b464-d6edf95813e4#:~:text=Important%3A%C2%A0New,Sovereign%20Exchange%20deployments.  for more information.
First, click File and Add Account. In the text box, please provide your METU e-mail address as usercode@metu.edu.tr. (The usercodes for students are in the form of e123456)

Please try automatic configuration first. After you click Connect, Outlook will configure required server settings and ask for your METU password. In the following window, you need to provide your user name without @metu.edu.tr part. Please delete that part and click OK and your METU e-mail address will be added to Outlook. 

If automatic configuration doesn't work, select IMAP and type the following server settings for incoming and outgoing mail.

If you need to change e-mail server settings, you can view your settings and alter them via File / Account Settings / E-mail links. The settings in File / Account Settings / Server Settings should look like the following:
Incoming server: imap.metu.edu.tr Port: 993 Encryption SSL/TLS
Outgoing server: smtp.metu.edu.tr Port: 465 Encryption SSL/TLS
Require logon using Secure Password Authentication (SPA) check box should be ticked for outgoing mail.
The following are related screenshots for Outlook 2010.
In order to read and send e-mail via Outlook which is installed with Microsoft Office package you should configure the settings on the central e-mail server.
Select "File" tab and click Account Settings. Select Account Settings  from the drop down list.
On "Account Settings" window, click New  on "E-mail" tab.

Then select "Manually configure server settings or additional server types" and click Next.

On the next window select "Internet E-mail" and click Next.

Write down your name, e-mail address, user name and password. If you want your password to be remembered on later entries, tick "Remember password" check box.
If you want to access your folders on the server and messages from multiple computers, choose "IMAP". If you want to download your inbox onto one single computer, access your messages only locally and you do not need to access your folders on the server, choose "POP3".

IMAP Settings:
Write down the incoming mail server as imap.metu.edu.tr, the outgoing e-mail server as smtp.metu.edu.tr and click  More Settings.

In order to use secure IMAP connection tick "My outgoing server (SMTP) requires authentication" check box on "Outgoing Server" tab on "Internet E-mail Settings" window.

On "Advanced" tab, the port number for "Incoming server (IMAP)" should be 993 and type of encryption should be SSL. The port number for "Outgoing server (SMTP)" should be 465 and type of encryption should be SSL.


POP3 Settings:
Write down the incoming mail server as pop3.metu.edu.tr, the outgoing e-mail server as smtp.metu.edu.tr and click  More Settings.

In order to use secure POP3 connection tick "My outgoing server (SMTP) requires authentication" check box on "Outgoing Server" tab on "Internet E-mail Settings" window.

On "Advanced" tab, the port number for "Incoming server (POP3)" should be 995 and type of encryption should be SSL. The port number for "Outgoing server (SMTP)" should be 465 and type of encryption should be SSL. If you don't want to download all messages at this time, tick "Leave a copy of messages on the server" check box.

After you finish configuring, when you click Next a test mail is sent in order to check the settings.


If you want to check or change the settings later, on "Account Settings" window select "E-mail" tab and click Change.

Note: This document is based on Microsoft Outlook 2010 version. Menus and options may vary with the previous versions.


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-use-metu-e-mail-services-microsoft-outlook

---

## Entry 2683

Question: How can I add my METU e-mail address to Gmail?
Answer: 

Go to mail.google.com and login with your username and password.
Click on the gearwheel symbol on the right up corner. Then click on the Settings on the new drop-down menu.

 
On the new page, click on the Accounts and Imports from the top menu.

Then click on the Add an email account next to the Check email from other accounts segment.

A new window will open. Enter your METU e-mail address on the textbox and click on the Next>> button.

On the next page, click on the Import emails from my other account (POP3) option. Then click on Next >> button.

On the next page fill in the related fields with appropriate information.
Username: Write your METU e-mail address (e******) Do not write your email alias, ie. name.surname combination, and do not include @metu.edu.tr part.
Password: Write your password.
POP Server: pop3.metu.edu.tr
Port: 995
Click on the option Always use a secure connection (SSL) when retrieving mail.
It is suggested that click on the Leave a copy of retrieved message on the server option. (Otherwise, all the mails might be moved from your METU e-mail account to Gmail.)
You can click on other options as you wish.


Your e-mail account has been added. Now, you are able to see your mails from your METU account on Gmail. If you don’t want to send mails on Gmail using your METU account, click on the option No and click on the Finish>> button.


If you want to send mails on Gmail using your METU account click on the option “Yes, I want to be able to send mail as” and click on the Next>> button.


On the new page, write your name in the textbox. If you want to treat as an alias click on the treat as an alias option. Then click on the Next Step>> button. 

On the next page, fill in the blanks with the appropriate information.
SMTP Server: smtp.metu.edu.tr
Port: 587
Username: Write your Metu mail username (e******)
Password: Write your password
Click on the Secured connection with TLS option.
If you are sure that all the information you entered are true then click on the Add Account>> button.

On the next page, you need to verify yourself. For this purpose, an e-mail is sent to your METU account. If you wish, you can click on the link which you will see on the e-mail or you can enter confirmation code on the textbox. If you entered the confirmation code, click on Verify button.

Now, you are able to send mails from Gmail using your METU account.


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-add-my-metu-e-mail-address-gmail

---

## Entry 2684

Question: How can I connect Windows mail to my METU mail address with IMAP?
Answer: 

Click on start button of Windows and write "mail". Then click mail software of Windows.

When you open the software, click on the symbol of three line which is located on the left upper corner of the screen.

Click Accounts.

On the left side click Add Account button.

Choose Advanced Setup.

And select "Internet email - POP or IMAP accounts that let you view your email in a web browser"


After that, fill in the blanks correctly according to your METU mail address information. When you finish click on Sign In button. Then close the window by clicking Sign in.




Link: https://faq.cc.metu.edu.tr/faq/how-can-i-connect-windows-mail-my-metu-mail-address-imap

---

## Entry 2685

Question: How can I use METU Central E-Mail Services with Pine?
Answer: 

Pine, as well as being an easy-to-use program for sending, receiving, and filing Internet electronic mail messages, it facilitates accessing to newsgroups through Newsgroups Service and supports many advanced features for users. 
To execute Pine program, you have to use a terminal program such as SSH. The terminal program enables you to login to the central server systems with a user code and a password. After you connect yourself to the servers with your login names and passwords, you have to enter pine command, on the command line of the system. You will be asked your user code and password, again. Now then, you are able to use Pine as displayed below. 

ATTENTION: When you are using SSH gibi terminal programs, the mouse will not operate. You should use the arrow keys of your keyboard to do your operations on Pine. 
• Reading e-mail messages:
On the main menu, selecting the following option, will enable you to view an index of incoming messages; 
 I MESSAGE INDEX - View messages in current folder
 To view the e-mail content, you should highlight the message you wish to read in the message list and click Enter 
• How to view the attachment file: 
To view the attachment of the e-mail you are reading, you should press V to display the attachment and then you should press S to save it on your user directory. To execute the file after you save the attachment file on your user directory, you should transfer the file to your computer via FTP program.
• Composing an e-mail message:
The following option on the main menu will enable you to compose an e-mail message and send it to the address you specified; 
C COMPOSE MESSAGE - Compose and send a message
Select this option with the arrow keys on your keyboard and click Enter. 
To: Enter the address of the recipient of your e-mail message in this field.
Cc: Enter the address of the recipient to whom you would like to send a copy of the e-mail message in this field.
Attchmnt: Add the attachment file you wish to send in this field. (You can select a file on your user directory by clicking firstly Ctrl+J and then Ctrl+T keys.)
Subject: Enter the subject of your e-mail message.
Message Text: Message text area contains the actual text of the email message. Write your message content in this section. 
 You must click Ctrl+X keys simultaneously to send the e-mail message. 
NOTE: You are not obliged to fill in the Cc and Attachment fields of your message every time you send a message. For example, you can compose and send a message as shown below; 
 To : usermetu.edu.tr Cc : Attchmnt: Subject : information request ----Message Text---- Hi, I'd like to get information about the services offered by Computer Center.
• Attaching a file to an e-mail message:
To attach an attachment file to an e-mail message you are composing, firstly, you should transfer the file to your user account via an FTP program. While composing the message, you should click the Ctrl+J and then Ctrl+T keys on the "Attchmnt" field to locate the place of your attachment file. Your user directory will be displayed. Highlight the file you wish to attach and click Enter twice. You will then return to the screen that diplays the message you are composing. You will notice that the attachment file is being shown in the "Attachment" field. 
• Creating an Address Book:
On the main menu, selecting the following option, will enable you to build a list of your regular e-mail correspondents, to create easily remembered "nicknames" for these addresses, and to quickly retrieve an email address when you are composing a message; 
 A ADDRESS BOOK - Update address book
 When you select this option, you should click  character to add new entry to your address book. You can fill in the spaces appropriately and then save the data with Ctrl+X keys.
• Viewing the sent-mail folder:
You should first click on the Mailboxes button, then you should click on the Sent button to view the list of the messages that you have sent.
• Reading e-mails in the OLDINBOX:
L FOLDER LIST - Select a folder to view 
option enables you to select a folder and see your messages in that folder. Among these folders are OLDINBOX.date folders. Highlight the OLDINBOX folder that you want look at and key in Enter  to see your e-mail. 
• Deleting an OLDINBOX: 
On the main menu; 
L FOLDER LIST - Select a folder to view 
Option lets you select the folders you want and see the message content. Among these are the OLDINBOX folders. You can delete the folder you choose by highlighting/selecting the folder and keying D (Delete) and then to confirm deletion keying Y (yes). 
• Reaching SPAMBOX:
On the main menu, the following option, will enable you to select any folder you would like to view. 
 L FOLDER LIST - Select a folder to view
 In these folders you may view your messages as well as your SPAMBOX directory. 
• Introducing the e-mails to the central spam filter which is believed that are considered as spam and saved to the SPAMBOX inaccurately: 
If you consider the e-mails that are saved to the SPAMBOX are not spam, you can send the content (body) of the e-mail, together with their   full header  information to Computer Center. In addition to this, it should be regarded that an e-mail which you would like to receive as a regular mail should not be in a category to be filtered as spam for each and every user, the e-mails that are not spam specifically for you shall be followed under the SPAMBOX folder.
• Preventing the display of "Terminal type ANSI is unknown" message:
If, immediately after logging onto your account with SSH program and entering the following command, you are receiving "Terminal type ANSI is unknown" message,
pine
you should enter the following command before you enter the "pine" command, to be able to log onto pine later on,
echo 
Then, you should check the information displayed and perform the following steps consequently. If you do not perform the following steps, you will always have to enter the following command to log onto pine program;
/usr/local/bin/pine
If you are using "Bash Shell" you should remove the "PATH" line in .profile, file, and if you are using "Tcsh Shell" you should remove the "PATH" line in .tcshrc file, or add :/usr/local/bin information to this variable. If "Terminal type "ANSI" is unknown" message is displayed once again, enter the following command,
echo 
and see which shell you are in currently. One of the following lines will be displayed:
/bin/ksh /usr/local/bin/bash /usr/local/bin/tcsh/
If the line displayed is one of the first two lines shown above(ksh,bash), enter the following command on the command line,
export TERM=vt100
If the line displayed is the third line shown above (tcsh), enter the following command on the command line;
setenv TERM=vt100
If you do not want to enter these commands once again each time you need them, for "bash" and "ksh", write the following command in .profile file,
export TERM=vt100
and for "tcsh", write the following command in .tcshrc file.
setenv TERM=vt100

• Viewing the full header of each incoming e-mail message:
If you would like to view the fullheader of the messages on the "Pine" program, the first thing to do is to select the following option with the arrow keys on the Pine screen;
S SETUP - Configure Pine Options
Then press C key on your keyboard; "Setup Configuration" menu will be displayed. Select "Configuration" option. On the Setup Configuration page, you will see "Set Feature Name" title at the somewhat lower part of the screen. Use the arrow keys to choose the "enable-full-header-cmd" under the very same title. Then, mark it with the Xkey. Exit with the E key.
Go to Inbox folder and open the message whose fullheader you wish to see. When you press H on your keyboard, you will be able to see the fullheader of your message. When you press H again, the fullheader will disappear.
If you would like to forward the fullheader of your message to another person, forward it directly without adding an attachment to the message. This method is most useful when you wish to report a spam mail to your system administrator.


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-use-metu-central-e-mail-services-pine

---

## Entry 2686

Question: How can I use METU E-Mail Services with Apple Mail?
Answer: 

You need to configure the mail settings on your MAC as follows in order to read and send e-mail via your Apple Mail application. First, start your Apple Mail.

If you don't have any email accounts set up previously, Apple Mail will ask you to choose a Mail account provider. Select "Other Mail Account" and click Continue.

Fill in your name, email address and password.

After clicking Sign in, type incoming and outgoing mail servers as follows:

If your password is correct, then Apple Mail will ask to select whether to use Mail and Notes with this account.

That will be all and you will see your current email messages.
If you have another email account already set up in your Apple Mail, then you need to select Accounts from the Mail menu and click + in the popup window to add your METU email.

If you have changed your METU user password, you need to update it in your Apple Mail. There are two steps to update your password.
1. First, select Preferences from the Mail menu.

Go to the Accounts tab.

In server settings, type your new password in both of the password fields.

2. Select Accounts from Mail menu and update the password in that popup window, as well.



Link: https://faq.cc.metu.edu.tr/faq/how-can-i-use-metu-e-mail-services-apple-mail

---

## Entry 2687

Question: How can I use METU E-Mail Services with iPhone or iPad?
Answer: 

You should configure the settings on the central e-mail server in order to read and send e-mail via your iPhone or iPad.
Select Settings > Mail, Contacts, Calendars and tap Add Account.

 

On "Add Account" screen select Other and on the next screen tap Add Mail Account.

 

On "New Account" screen write down your name, e-mail address and password and tap Next. Wait until your account is verified.

 

If you want to access your folders on the server and messages from multiple devices such as computer, mobile phone etc. choose "IMAP". Write down the incoming mail server as imap.metu.edu.tr. If you want to download your inbox onto your device, access your messages only locally and you do not need to access your folders on the server choose "POP". Write down the incoming mail server as pop3.metu.edu.tr.
For both options, write down the outgoing mail server as smtp.metu.edu.tr. Enter your user name and password for both servers and tap Next.

 

While your user name and password are being verified, tap Continue on the warning on the screen. If you have chosen IMAP, make sure that "Mail" switch is ON to be able to send and receive e-mails. Tap Save to save the settings.

 

If you want to check or change the settings later, select Settings > Mail, Contacts, Calendars. Choose your account under "Accounts". On the next screen tap your e-mail address.

 

In order to check or change outgoing mail server settings, tap "SMTP" on "Account" screen. You can see the settings when you tap "smtp.metu.edu.tr" address. "Use SSL" option should be ON, "Authentication" should be Password and the port number should be 587.

 

In order to check or change incoming mail server settings, tap "Advanced" on "Account" screen. Port numbers should be 993 for IMAP and 995 for POP. For both options "Use SSL" option should be ON and "Authentication" should be Password.

 

 

Link: https://faq.cc.metu.edu.tr/faq/how-can-i-use-metu-e-mail-services-iphone-or-ipad

---

## Entry 2688

Question: How can I use METU E-Mail Services with Mozilla Thunderbird?
Answer: 

You should configure the settings on the central e-mail server in order to read and send e-mail via Mozilla Thunderbird.
Open "Account Settings" window by selecting Tools > Account Settings from the menu. Then click Account Actions, select Add Mail Account from the drop down list in order to open "Mail Account Setup" window (This window will automatically appear when you initially start Mozilla Thunderbird).
Write down your name, e-mail address and password to the boxes in the window and click Continue. If you want your password to be remembered on later entries, tick "Remember password" check box.

Mozilla Thunderbird defines default server settings automatically. Click Create Account to use these settings.
To change the default settings click Manual config. If you want to access your folders on the server and messages from multiple computers, choose "IMAP". If you want to download your inbox onto one single computer, access your messages only locally and you do not need to access your folders on the server, choose "POP3".
In order to use secure IMAP connection the port number should be 993, connection security (SSL) should be SSL/TLS and authentication method should be Normal Password.
In order to use secure POP3 connection the port number should be 995, connection security (SSL) should be SSL/TLS and authentication method should be Normal Password.
For both options, the outgoing server name should be smtp.metu.edu.tr, port number should be 465, connection security (SSL) should be SSL/TLS and authentication method should be Normal Password. 

If you want to check or change the settings later, open "Account Settings" window by selecting Tools > Account Settings from the menu. Then select "Server Settings" under your account from the list on the left frame.

Note: This document is based on Mozilla Thunderbird 7.0 version. Menus and options may vary with the previous versions.


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-use-metu-e-mail-services-mozilla-thunderbird

---

## Entry 2689

Question: How can I use METU E-Mail Services with my Android installed device?
Answer: 

You should configure the e-mail application with the METU e-mail settings in order to read and send e-mail via your device.
Start the e-mail application on your phone and select add account. Write down your e-mail address and password and tap Manual setup. Choose the account type on the next screen. To access your folders on the server and messages from multiple devices such as computer, mobile phone etc. choose "IMAP". 

 

If your mobile device discovers the server information, please use them as is. If you have problems with auto discovery, you can then use the following settings.
On "Incoming server settings" screen, write down the server name as imap.metu.edu.tr and port number as 993 for IMAP or write down the server name as pop3.metu.edu.tr and port number as 995 for POP3. For both options, select the security type SSL (Accept all certificates).

 

On "Outgoing server settings" screen, write down the server name as smtp.metu.edu.tr and port number as 465. Select the security type SSL/TLS (Accept all certificates) and tick Require sign-in check box. On the next screen define the account options. On the final screen write down the name that is going to be displayed on outgoing messages and tap Done to save the settings.

 

 

Link: https://faq.cc.metu.edu.tr/faq/how-can-i-use-metu-e-mail-services-my-android-installed-device

---

## Entry 2690

Question: How can I use METU E-Mail Services with Windows Mail?
Answer: 

You should configure the settings on the central e-mail server in order to read and send e-mail via Windows Mail which is installed on Windows Vista.
Open "Internet Accounts" window by selecting Tools > Accounts from the menu. Then click Add and select E-mail Account.

Write down your name and click Next  on the next window (This window will automatically appear when you initially start Windows Mail).
Write down your e-mail address and click Next  in order to open the server settings window. If you want to access your folders on the server and messages from multiple computers, choose "IMAP". Write down the incoming mail server as imap.metu.edu.tr.

If you want to download your inbox onto one single computer, access your messages only locally and you do not need to access your folders on the server, choose "POP3". Write down the incoming mail server as pop3.metu.edu.tr.

For both options, write down the outgoing e-mail server as smtp.metu.edu.tr, tick "Outgoing server requires authentication" check box and click Next .
Write down your user name and password on the next window. If you want your password to be remembered on later entries, tick "Remember password" check box. Click Next  in order to finish the configuration on the next window.

In order to use secure IMAP connection click Properties on "Internet Accounts" window. Select  Advanced tab, write down the port numbers 587 for "Outgoing mail (SMTP)" and 993 for "Incoming mail (IMAP)". Tick the both "This server requires a secure connection (SSL)" check boxes.

In order to use secure POP3 connection click Properties on "Internet Accounts" window. Select  Advanced tab, write down the port numbers 587 for "Outgoing mail (SMTP)" and 995 for "Incoming mail (POP3)". Tick the both "This server requires a secure connection (SSL)" check boxes. If you don't want to download all messages at this time, tick "Leave a copy of messages on server" check box.


If you want to check or change the settings later, open "Internet Accounts" window by selecting Tools > Accounts and click Properties.
Note: This document is based on Windows Mail 6.0 version. Menus and options may vary with the previous versions.


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-use-metu-e-mail-services-windows-mail

---

## Entry 2691

Question: What is the difference between POP3 and IMAP accounts?
Answer: 

POP and IMAP are communication protocols that download your e-mails to your personal computer or other devices.
POP3It provides basic downloading and deleting actions. E-mail service providers who use POP usually take actions as follows; connect to the server, get all the messages, keep those messages on the user’s device and delete them from the server, disconnect to server. Therefore, when mails are also deleted from the device, they are no longer available. However, some e-mail service providers may provide an option to archive those messages in a new folder. POP3 supports only one user at a time. In fact, if you connect to your account from a second device then it disconnects the first one.
IMAPWhen several devices are connected to a mail service provider at the same time, IMAP protocol prevent some possible problems with these devices to occur. Unlikely to POP, IMAP provides bidirectional communication. Thus, some possible problems are inhibited that may occur while connecting on web, synchronizing from mobile devices, getting e-mails from computer. The most useful function of IMAP is that when you move a mail to a new folder then it updates all the connected devices. All the modifications are updated from all connected devices synchronously.
 


Link: https://faq.cc.metu.edu.tr/faq/what-difference-between-pop3-and-imap-accounts

---

## Entry 2692

Question: How can I add an e-mail address to the black list?
Answer: 

Go to https://horde.metu.edu.tr/login.php address and login with your username (e******) and password. If the language is not appropriate for you, choose the language from the “Dil” drop-down menu. Then, click on the “Giriş” button.
To use the feature first the "Mail" icon and then "Filters" icon are clicked.

From the menu on the left, click on the "BlackList" button. 

Choose the action for blacklisted addresses.  1) If you want to delete messages from the addresses you will add on the blacklist then you should choose “Delete message completely” option. 2) If you want those messages only be marked rather than deleted then you should choose “Mark message as deleted” option. 3) If you want to send messages from addresses that you will add on blacklist to some folders (Inbox, draft, sent mail, trash) then you should choose “Move messages to folder:” option and select the folder name from the drop-down menu next to the “Move messages to folder:” option.
Click inside the textbox at the bottom. Now, write down e-mail addresses that you want to put in black list. (Be careful: You should write all the e-mail addresses on separate lines.)
 
When you finish writing e-mail addresses, click on the "Save" button on the same page.
Changes are saved. E-mail addresses are on the blacklist and the action you selected will be applied to the emails sent from those email addresses.
 
 

Link: https://faq.cc.metu.edu.tr/faq/how-can-i-add-e-mail-address-black-list

---

## Entry 2693

Question: How can I add someone to the white list?
Answer: 

Go to https://horde.metu.edu.tr/login.php address and login with your usercode and password. If the language is not appropriate for you, choose the language from the “Dil” drop-down menu. Then, click on the “Giriş” button.
To use the feature first the "Mail" icon and then "Filters" icon are clicked. 





From the menu on the left, click on the "White List" button. 





You will see a textbox. Click inside the textbox. Now, write down e-mail addresses that you want to put in white list. (Be careful: You should write all the e-mail address on separate lines.)
When you finish writing e-mail addresses, click on the "Save" button on the same page
Changes are saved. E-mail addresses are on the whitelist.
 


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-add-someone-white-list

---

## Entry 2694

Question: How can I save e-mail attachments with Horde?
Answer: 

In Horde web e-mail application, by default, e-mail attachments are not saved along with the e-mail in the sent mail folder. In order to save attachments with your e-mail:
in the compose window, click the arrow next tothe Add Attachment sign and select "Save Attachments in Sent Mailbox". This setting will save the attachments, only for the current e-mail.

to enable saving attachments for all e-mails
after logging in, click the cog in the menu, Preferences --> Mail --> Sent Mail --> and select "Save Attachments" in "Save attachments in the sent-mail message?" box. Now, e-mail attachments in your future e-mails will be saved with the e-mail message.




Link: https://faq.cc.metu.edu.tr/faq/how-can-i-save-e-mail-attachments-horde

---

## Entry 2695

Question: How can I use METU Central E-Mail Services with Horde?
Answer: 

Horde is a service that can be used to connect to your user account on the central servers of METU and easily perform activities such as, accessing your e-mails, organizing your work using applications of a calendar, tasks, slips, or making password changes, and uploading files. The service can be accessed from the http://metumail.metu.edu.tr/ address by clicking on the relevant link (Fig. 1) or direct from the https://horde.metu.edu.tr/ address (Fig. 2).

Figure-1
Figure-2

The related e-mail application help files of the Horde service may be accessed by first running the program, next, clicking the "Mail" icon and then clicking on the "Help" icon. 



Link: https://faq.cc.metu.edu.tr/faq/how-can-i-use-metu-central-e-mail-services-horde

---

## Entry 2696

Question: How do I filter my incoming e-mails with Horde?
Answer: 

To prevent unwanted mail to take up space in the "Inbox" or to automatically transfer e-mail messages from certain people and/or about certain topics the "Filters" feature of Horde may be used. To use the feature first the "Mail" icon and then "Filters" icon are clicked. 






In the Filter Rule page, to create a new rule, please click "New Rule".
You need to provide a name for the new rule.
In the For an incoming message that matches part, you can define criteria for To, Subject, Sender, From, etc.
In the Do this part, you can define the action for the e-mails matching the criteria.  Deliver to folder, Delete message completely, Redirect to... are frequently used actions.

In the above screenshot, the rule delivers the emails where TO field contains genel-duyurumetu.edu.tr to the folder duyurular.








Link: https://faq.cc.metu.edu.tr/faq/how-do-i-filter-my-incoming-e-mails-horde

---

## Entry 2697

Question: I blacklisted someone by accident in my Horde Webmail. How do I undo that?
Answer: 

Log into Horde Webmail on browser with your username and password.
Choose Options from the Menu Bar on the left.
In the Options Section, click on Filters.
Click on Blacklists from the Menu on top of the browser
Click on Edit your filter rules.
Select the rule(s) or e-mail addresses that you wish to remove and delete them.
After the changes click Save button.
 

Link: https://faq.cc.metu.edu.tr/faq/i-blacklisted-someone-accident-my-horde-webmail-how-do-i-undo

---

## Entry 2698

Question: What are the options for displaying a mailbox?
Answer: 

The Mail Preferences option in the settings (gear icon) in Horde menu lets you customize the preferences for Mail and Mailbox Display.

With Mailbox Display Preferences submenu, you can set the mail sorting criteria, messages per page, etc. according to your needs.If you see an unread mail at the top, instead of new mails, you should select First Page from the options in the When opening a mailbox for the first time, where do you want to start? box.



Link: https://faq.cc.metu.edu.tr/faq/what-are-options-displaying-mailbox

---

## Entry 2699

Question: How can I add a signature in Roundcube?
Answer: 

Login to Roundcube Webmail. Click on the "Settings" button and then click on the "Identities" button. After choosing your username, add your signature - you want to display it automatically in your e-mail - to the message box. Finally, click on the "Save" button.


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-add-signature-roundcube

---

## Entry 2700

Question: How can I change user interface settings (Language, time zone, time format, date format, etc.) in Roundcube?
Answer: 

Login to Roundcube Webmail. Click on the "Settings" ("Ayarlar" in Turkish) button, the "Preferences" ("Tercihler" in Turkish) button, and the "User Interface" button, respectively. In the "Main Options" ("Temel Ayarlar" in Turkish) section, you can adjust language, time zone, time format, date format, etc.


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-change-user-interface-settings-language-time-zone-time-format-date-format-etc

---

## Entry 2701

Question: How can I create and edit my address book in Roundcube?
Answer: 

To edit your address book in Roundcube, click the "Contacts" button in the main menu. By using the "Add" button on the screen that will open, you can add new e-mail addresses and other information (phone, address, note, etc.) about these people to the defined contacts. You can save the information you entered by clicking the "Save" button.
You can upload the existing address book to Roundcube with the help of the "Import" button. The "Import" button, which will appear when the add contacts window opens, allows address books (saved in vCard and CSV (comma-separated data) file formats) to be imported into Roundcube.
You can use the "Export" button to export the contacts in your address book in Roundcube. When you click this button, your contacts saved in Roundcube will be downloaded to your computer as a ".vcf" file.
Your address book and registered contacts that you previously created in Squirrelmail (sqrl.metu.edu.tr) will be copied to Roundcube after you log in to the Roundcube interface for the first time. However, after you log into the Roundcube interface for the first time, the address books in the Squirrelmail and Roundcube interfaces will continue to work independently.


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-create-and-edit-my-address-book-roundcube

---

## Entry 2702

Question: How can I delete my e-mails using Roundcube?
Answer: 

Using Roundcube, you can delete all messages in a mailbox or specific messages of your choosing.
When you click on the "Delete" button on the screen after selecting the e-mails you want to delete, these e-mails will be moved to the "Trash" folder.
You must also delete the e-mails from the "Trash" folder that you want to completely delete from your account. You can reach the "Trash" folder by clicking the "Trash" button in the "Mail" tab in the main menu. When you select the e-mails in the "Trash" folder that you want to delete completely and click the "Delete" button, these e-mails will be deleted directly without being moved to another folder.
You can have your e-mails sent to the "Trash" folder automatically deleted when you log out. To do this, click the "Server Settings" button in the "Settings" tab in the main menu, select the "Clear Trash on logout" option in the "Maintenance" section and save it. E-mails that you delete from your Inbox or other folders while you're signed in and that have been moved to Trash will be automatically deleted from Trash when you sign out.


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-delete-my-e-mails-using-roundcube

---

## Entry 2703

Question: How can I filter incoming e-mails in Roundcube?
Answer: 

Roundcube's "Filters" feature can be used to prevent spam from taking up space in the "Inbox" folder or to automatically move e-mails from certain people and/or certain topics to certain folders.
To use this feature, after entering Roundcube, first click the "Settings" button on the main panel and then the "Filters" button.
Warning: The filters defined in the Horde, one of the METU webmail interfaces, can also be viewed and used from the Roundcube interface. New filters to be defined in Roundcube are added to the filter set previously defined in the Horde interface. On the other hand, filters created in Roundcube are deleted when filters are edited by logging into the Horde interface again after the filter is created in Roundcube. Although it is planned to eliminate this problem when the testing phase of the Roundcube interface is completed, we recommend our users to be careful about this issue.


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-filter-incoming-e-mails-roundcube

---

## Entry 2704

Question: How can I send an e-mail using Roundcube?
Answer: 

Click on the "Compose" button. After composing your e-mail with the recipient's e-mail address(es), subject, and message, you can send it by clicking the "Send" button. If you want to finish your e-mail later, you can save your message to the "Drafts" folder by clicking the "Save" button. When you decide to send your saved e-mail, click on the "Drafts" folder and find the e-mail you want to continue composing.


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-send-e-mail-using-roundcube

---

## Entry 2705

Question: How can I use METU Central E-Mail Services with Roundcube?
Answer: 

Roundcube is a webmail service to facilitate access to electronic mail services provided on central servers from within or outside METU via a modern interface by means of a web browser (Mozilla Firefox, Chrome etc.). The service can be accessed from the http://metumail.metu.edu.tr/ address by clicking on the relevant link or direct from https://webmail.metu.edu.tr/ address.


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-use-metu-central-e-mail-services-roundcube

---

## Entry 2706

Question: New Students
Answer: 

Brief Information on IT Services for new students
You can visit http://map.metu.edu.tr/ for METU Interactive Map.

 
If you are new registered student at METU
New students at our university are required to visit https://useraccount.metu.edu.tr/newstudent and create their user codes and passwords. You can then use METU IT Services with your user code and password. Please use email addresses other than hotmail.com, live.com or outlook.com.
All of METU IT Services are used with METU user codes.  (e.g. e123456, you cannot logon to any METU IT Service with METU e-mail aliases like name.surname@metu.edu.tr)
If you were a student at METU previously
If you were a former student of METU and re-registered within an absence of one semester, you can use your previous user code and password. If you were not registered for more than a semester, you need to follow the steps for newly registered students. If you are a former student and did not recall your password, you can visit useraccount.metu.edu.tr and click "Forgotten your password?" link.
User Codes
To be able to use the IT resources of METU, you need to have a user code and a password. With your user code and password, you can use METU IT Services like, Student Affairs Information System, ODTÜClass, wired and wireless network, PC rooms, etc.
Your user code is the first 6 digits of your student ID, starting the letter "e". (If you have a student ID like 123456-7, then your user code is e123456)
For general information about user codes and passwords, please visit http://usercode.cc.odtu.edu.tr.
The user codes are required to be used in accordance with METU Information Technology Resources Use Policy, which is available from http://www.metu.edu.tr/it-use-policy
Passwords
You can use METU User Account Management page, https://useraccount.metu.edu.tr, to be able to change your passwords. If you forgot your password, please follow the instructions on https://faq.cc.metu.edu.tr/faq/i-forgot-my-password-where-can-i-apply 
Wired and wireless networks
https://faq.cc.metu.edu.tr/faq/there-wireless-network-metu-how-can-i-connect
Users may connect to either eduroam or meturoam wireless network.
Information Security
FAQs about information security and things to consider:
https://faq.cc.metu.edu.tr/groups/information-security
 


Link: https://faq.cc.metu.edu.tr/faq/new-students

---

## Entry 2707

Question: Bubble Sheet Assignments in Gradescope 
Answer: 

Bubble Sheet Assignments
Gradescope’s bubble sheet assignments allow you to create a multiple-choice answer key for the automatic grading of your students’ submissions. 
You need to use Gradescope’s 200-question bubble sheet template for student submissions. The provided PDF template includes the following fields:
Name - used for auto-matching uploaded submissions to students on your roster
ID - student ID, if applicable it can be used for auto-matching uploaded submissions to students on your roster
Section - enter a section name if applicable
Date - date the student completed the assignment
Version - used for the student to mark which version of the assignment they are assigned to
Other - a field to enter any other information you have requested from your students
Two hundred answer spaces - provided over two pages; only upload the used pages 
The template cannot be customized to contain question/answer content. You will need to provide students with a question list and multiple-choice answers outside of Gradescope.

To create a bubble sheet assignment:
Access your course dashboard and select Assignments from the left navigation menu.
Select the Create Assignment button from the taskbar at the bottom of the page. 
Select Bubble Sheet from the list of assignment types and then select Next at the bottom of the page. 
For more information on bubble sheet assignments, please visit https://help.gradescope.com/article/gkwvq606fq-instructor-assignment-bub... .
Uploading Scans
You can use any scanner to create PDFs of your answer sheets. Check out scanning tips from Gradescope .
Once you have your PDFs ready to upload, click Select PDF Files on the Manage Scans page.
Select your files and they will begin uploading. You can also drag and drop submissions directly onto the Manage Scans page. It's recommended that you upload PDFs that contain multiple student submissions for faster processing.
As soon as submissions are created on the Manage Scans page, Gradescope automatically attempts to match each submission to a student in the roster, using the Name and ID regions that you set up in the Edit Outline step. 
Answer Key
On the Answer Key page, allocate the correct answers to each numbered question for your assignment. You can create multiple versions of the same bubble sheet assignment, each having individual answer keys.



Link: https://faq.cc.metu.edu.tr/faq/bubble-sheet-assignments-gradescope

---

## Entry 2708

Question: Cisco Webex for e-School
Answer: 

With the initiation of the distance education process, Cisco Webex application was temporarily opened for use by our University in order to meet the online meeting and web conferencing needs that may be experienced in addition to the courses. Registered users can create meetings and invite unregistered people to the meeting.
The registration process required for the application to be used is carried out by the Computer Center.
In order to apply, the pre-registration form at https://bidb.metu.edu.tr/forms/cisco-webex-kullanimi must be filled out. You can access the form with your METU user code and password. The pre-registration form is accessible to our faculty members. Currently, research assistants and part-time faculty members do not have access.
When you click the "Submit" button on the pre-registration form, your membership request will be received and a message will be sent to your METU corporate e-mail address for your membership to start to use Webex. (Registration cannot be done automatically. Your registration will be done as soon as possible.)
After the registration confirmation is done by the Computer Center, you can create your password with the link in the e-mail you will receive, download the program from the left-hand menu at https://metu.webex.com and start the meeting.
Participation of Students to the Course / Web Conference:
Students do not need to have a Webex account to participate in the course. They can join as a guest.
Students can install the Webex application on their mobile device, tablet or PC at https://metu.webex.com. Clicking on the link in the course invitation sent by the teacher through various communication channels (e-mail, METUClass, etc.), this application is automatically opened and participation is provided.
If the students click on the link to be sent without installing any application, they can participate in the training via the web browser. The student participates in the course by entering his / her name, surname and e-mail address.
Note: Some old version web browsers may not connect to Webex. In this case, the student will need to install the free Webex application.
Online Meeting / Web Conference Use for Teachers:
1 - Account Activation E-mail

2- Password Creation Page

3- Webex Application Download Page
You can download and install the Webex application according to the type of your operating system from the page that comes after creating your password. You can also install Webex for mobile devices and tablets from app stores (Google Play, Apple Store). It is possible to use https://metu.webex.com to access related pages later.

4- Webex Login Page
After installing the application you downloaded on your device, run it and enter your METU corporate e-mail address. In the next step, enter your password created for Webex.

5- Webex Site Selection
You should select metu.webex.com address as Webex Site. 

6- Webex Meeting Screen - Start a Meeting
If your login information is correct, the application will open. You can select the Start Meeting option to start a meeting. If you are going to be a participant, enter your meeting information given to you in the "Joining a Meeting" section.

7- Webex Meetings - Meeting Screen
After pressing Start Meeting, screens related to camera and microphone settings may appear, you can continue by checking the settings here. If someone else has not yet joined your meeting, a white screen with the text "Waiting for others to join" will appear.

8- Webex Meetings - Invitees to the Meeting
When the people you invite join the meeting, the audio and video of the participants are enabled due to the Webex default settings. If the guests did not turn off their audio and video on their settings before connecting to the meeting, you can change them as the Host.
9 -Webex Meeting - Participant Menu
If you turn off "Anyone Can Share" feature from the "Participant" menu of the application, only you or the participants you have privileged will be able to share.

10 Webex Meeting - View Menu
You can turn off the video of the participants by turning off the "Show Participant Video" feature from the View menu.

About Cisco Webex
Webex is an optimal solution for smartworking and distance learning.This document takes into account two main scenarios that are addressed by specific Webex applications for each scenario:
Distance lesson (virtual class)Focus on real-time collaboration between teacher and students with audio/video, application sharing, multimedia content, annotation and polls: Webex Meetings.In this scenario, students can join the lesson in guest mode, that is, without having to create a Webex account.
Collaboration between teachers and staff of the School InstituteAdvanced document chat and sharing capabilities in a more structured environment in addition to audio/video collaboration and screen sharing: Webex Teams.
Description of the setup process (preliminary)
TeacherThe teacher receives the welcome email -> click to set the password and install the Webex Meetings appStudentThe student installs Cisco Webex Meetings on their iPad/tablet/mobile device without having to create a Webex account
Setup for the teacher 
Click "activate" in the welcome emailThe browser opens, allowing the teacher to enforce their password
The Webex page loads in the browser
Click "Download" to download the Webex Meetings App and install it
Teacher login
Launch the Webex Meetings app on your PC and log in using your Webex credentials (email address and password)
Virtual lesson
The virtual lesson takes place in a virtual classroom represented by the so-called "Personal Room" or personal room of the teacher.This room represents the physical class of the school and the Personal Room provides digital tools that allow an advanced collaboration between teacher and students. Teachers can share their PC screen, show documents, applications, and even multimedia content.The Personal Room is run by the teacher. The teacher initiates the lesson by allowing the students to participate. The teacher can also mute or even expel one or more students and can record the lesson itself, to allow students who are absent to enjoy it later. The teacher can lock (equivalent to locking the classroom door) to prevent other students from connecting and finally, it is always the teacher who has the power to finish the lesson, closing the Personal Room.
How to use:
The professor organizes the video conference for the class using the link to WebexThe professor copies the Webex link of his/her Personal Room from the Webex appThe professor shares the link with the class through the most appropriate tool (electronic register, email etc)At the indicated time, the professor starts the meeting; students participate by clicking on the received linkStudents who connect in advance (before the professor starts the meeting) are waiting. They are equally waiting when the professor locks the meeting.
Lesson in progress (teacher side)
Clicking on "Start Meeting" (see slide above) starts the video preview to allow the teacher to verify that his video is ok. 
Clicking again on "Start Meeting" starts the actual lesson, with audio and video. As long as no student has connected Webex shows the white screen, with the teacher's video at the bottom of the page.
Student Participation
Premise: The student installed the Webex Meetings app and received, by email for example, the link to the lesson (link of the Personal Room)
Clicking on the link launches the Webex appThe student enters their first and last name and an email address -> click on "join meeting"(note: Webex account is not required, so no password is needed, and the email is purely informative)
The preview starts -> click "Join" to enter the virtual class
Note: With a non-standard browser, you may need to open the Webex Meetings app and insert the link to the lesson.
Lesson control (for the teacher)
The teacher can, through the list of participants, mute and possibly even expel the students individually. 
In addition, the teacher can turn off the camera during the lesson, share content, read what is written on chat screen, write a reply, survey (polling), share screen or application.
The teacher can, at any time, block access to the Personal Room by preventing additional participants (e.g. students of a different class) from entering. In the same way, the teacher can unlock it at any time. 
Only the teacher can finish the lesson. The teacher is also entitled to leave the Personal Room without the lecture ending, but in this case he will have to indicate another participant to take the lead on his/her behalf.
You can e-mail to odtuclass@metu.edu.tr for your questions and issues about Cisco Webex.


Link: https://faq.cc.metu.edu.tr/faq/cisco-webex-e-school

---

## Entry 2709

Question: How can I change my photo?
Answer: 

ID Photo
The photo you have in the Smart Card and the photo in IT systems should be the same due to the administrative decision taken by our university. For this reason, it is not possible to change your photo through IT systems.
Users who do not have a photo stored in the system or who want to change their photo can apply for a new smart card via "223 Smart Card Application Program". Your photo in IT systems is automatically updated when your smart card is formatted and ready.


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-change-my-photo

---

## Entry 2710

Question: How can I install Safe Exam Browser to the computers in my PC room? 
Answer: 

You can download the SEB for Windows Installation setup program (also containing the SEB Windows configuration tool) from SEB website. After download is completed, start SafeExamBrowserInstaller.exe and follow the steps in the installation program. The installation is straighforward.
After the installation, you need to configure the software with SEBConfigTool.exe located in the SEB application folder (usually C:\Program Files or C:\Program Files (x86)).
In most cases, you need to set only the settings in the General pane (like the URL which SEB opens and the passwords to open a config file for editing and to quit/restart SEB) and leave the default values for all other settings which present "secure" options. You also need to enable Safe Exam Browser setting from ODTÜClass. https://safeexambrowser.org/windows/win_usermanual_en.html#LMS
Once you have a config file for your browser, you can share it to all of your examinees, either by a .SEB file or by online (publish the config file from your website). They can complete the settings on their own computers with this link. 


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-install-safe-exam-browser-computers-my-pc-room

---

## Entry 2711

Question: How can I join an exam with Safe Exam Browser?
Answer: 

You can download the SEB for Windows Installation setup program (also containing the SEB Windows configuration tool) from SEB website. After download is completed, start SafeExamBrowserInstaller.exe and follow the steps in the installation program. The installation is straighforward.
After the installation, you need to configure the software with SEB Config Tool shortcut in the start menu or the SEBConfigTool.exe file located in the SEB application folder (usually C:\Program Files or C:\Program Files (x86)).

You can provide the settings file provided by your instructor either by
entering the URL in the Start URL text box
locating the configuration file via File / Open Settings  
After this step, please close the Config Tool and start Safe Exam Browser.


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-join-exam-safe-exam-browser

---

## Entry 2712

Question: How can I update my information in the Phonebook?
Answer: 

To update your personal web address and phone number in the Phonebook (https://phonebook.metu.edu.tr) you must first login to the system with your user name and password:

By clicking on the "Control Panel" (Kontrol Paneli) link on the screen after logging in, you can enter your personal web address and phone number from the fields that appear below; or if you have previously added information, you can change it. "Güncelle" (Update) button should be clicked to save the information.

The information viewed on this screen belonging to you, other than your personal web address and phone number, is automatically transferred from the Human Resources Management System (IKYS) under the Directorate of Personnel.


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-update-my-information-in-the-phonebook

---

## Entry 2713

Question: Where can I find information about ReCaptcha image validation (I'm not a robot) on the registration page?
Answer: 

Google ReCaptcha service is added to the user's browser automatically and verified by Google. In addition, since this service has a timeout, the verification may time out by itself when the correct ones are selected from the images shown on the screen and waiting for a while.
In addition to these, accesses from different IP addresses, some extension used in the browser, opening many pages in the incognito tab, wrong selections in the images provided by the ReCaptcha service may cause more information to be requested and verification images to be shown in order to prove that you are not a robot in subsequent verifications.
You can experience how the Google ReCaptcha service works outside the registration page by accessing https://www.google.com/recaptcha/api2/demo?invisible=false and experience the image verification service that will appear on the screen by opening the same address in an incognito tab.
In some cases, there are inconsistencies between the information requested by the ReCaptcha verification service and the images displayed on the screen. For example, when the service requests you to select a fire hydrant in verification, there may not be a fire hydrant in the pictures shown. In such a case, it is necessary to proceed to the next verification by clicking skip. We do not interfere with the Google ReCaptcha verification service used on our registration page.


Link: https://faq.cc.metu.edu.tr/faq/where-can-i-find-information-about-recaptcha-image-validation-im-not-robot-registration-page

---

## Entry 2714

Question: Although I uploaded the transcript of my undergraduate education in accordance with the format (pdf, 312kb) during the graduate application, why can I only view the first page after submitting?
Answer: 

Files uploaded in the graduate application program are displayed as a single page since they are brought as preview on the 'Final Stage' page. The real image of the uploaded files can be downloaded and viewed from the uploaded page. You can view the transcript document as two pages on the Academic Information page.


Link: https://faq.cc.metu.edu.tr/faq/although-i-uploaded-transcript-my-undergraduate-education-accordance-format-pdf-312kb-during

---

## Entry 2715

Question: Do I have to enter a recommendation letter for every applied program?
Answer: 

 You have to enter the names of professors or supervisors from whom you have obtained the recomendation letters (two letters , therefore two entries are required - please see here. )


Link: https://faq.cc.metu.edu.tr/faq/do-i-have-enter-recommendation-letter-every-applied-program

---

## Entry 2716

Question: For which department applications portfolio is required and when and where those should be submitted?
Answer: 

You can add your portfolio to the additional document module.


Link: https://faq.cc.metu.edu.tr/faq/which-department-applications-portfolio-required-and-when-and-where-those-should-be-submitted

---

## Entry 2717

Question: How can I apply to a new program?
Answer: 

If you are applying to a new program click the ‘Apply New Program’ button in the ms-phd applications page.


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-apply-new-program

---

## Entry 2718

Question: How can I get help for technical errors encountered during the application?
Answer: 

Please send your questions or problems about application to graduate programs via Information Request about METU Graduate Programs Application form.


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-get-help-technical-errors-encountered-during-application

---

## Entry 2719

Question: How can I update the information for the applied program?
Answer: 

a. Once you finish filling forms and uploading documents, you will see all the information you entered on a page after you select submit menu. Read them carefully for any mistake.
b. When you are sure that all the information is correct for the department/program you are applying, press the ‘SUBMIT’ button to finalize your application form.
c. Your application will be forwarded to the institute(s) for final control after the application deadline.
d. In an unlikely event that you need to change anything BEFORE the deadline, you can make changes as you wish. Make sure that you press ‘SUBMIT’ button to finalize again.
e.You can make any changes any time until the application deadline. All the information and the documents you submitted are automatically saved once you enter the program with your password. If you make any changes after pressing Submit button, please re-Submit them so they could be considered.
f. Do not forget that you will not be able to change anything after the deadline.


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-update-information-applied-program

---

## Entry 2720

Question: How do I upload my transcript?
Answer: 

For PhD applications, you need to upload two documents, Undergraduate and Master transcripts, to the Transcript upload field in related page. If your Undergraduate and Master transcripts are in one document, you should upload the same document twice.


Link: https://faq.cc.metu.edu.tr/faq/how-do-i-upload-my-transcript

---

## Entry 2721

Question: How to apply to a program? Can you explain the steps briefly?
Answer: 

You should follow the "How to Apply" steps from "Application for Admission to Graduate Programs at METU" main page.
 


Link: https://faq.cc.metu.edu.tr/faq/how-apply-program-can-you-explain-steps-briefly

---

## Entry 2722

Question: I do not prefer to enter my TCK No. What will be the consequences?
Answer: 

If you are a Turkish candidate entering the system as a foreign applicant, your application will be rejected due to providing misinformation.


Link: https://faq.cc.metu.edu.tr/faq/i-do-not-prefer-enter-my-tck-no-what-will-be-consequences

---

## Entry 2723

Question: I want to use the most up-to-date / highest grade I entered before / later, instead of my ALES result withdrawn from the system. What should I do?
Answer: 

By deleting the ALES grade you do not want, you can enter the high grade ALES result you want yourself.


Link: https://faq.cc.metu.edu.tr/faq/i-want-use-most-date-highest-grade-i-entered-later-instead-my-ales-result-withdrawn-system-what

---

## Entry 2724

Question: I was a graduated/not registered METU student and I didn’t apply before, how can I apply?
Answer: 

If you are graduated/not registered METU student, you should follow the "STEP.2: Choose Applicant Type" step from "Application for Admission to Graduate Programs at METU" mailn page.


Link: https://faq.cc.metu.edu.tr/faq/i-was-graduatednot-registered-metu-student-and-i-didnt-apply-how-can-i-apply

---

## Entry 2725

Question: Is it possible to apply a graduate program without ALES/GRE exam information?
Answer: 

A valid and recognized ALES/GRE exam result must be submitted with the application. Please refer to the related institute web page for information on these exams.


Link: https://faq.cc.metu.edu.tr/faq/it-possible-apply-graduate-program-without-alesgre-exam-information

---

## Entry 2726

Question: Is it possible to apply a graduate program without the English proficiency exam result?
Answer: 

A valid and recognized exam is required to be submitted with application. Please refer to the related institute web page for information on these exams.


Link: https://faq.cc.metu.edu.tr/faq/it-possible-apply-graduate-program-without-english-proficiency-exam-result

---

## Entry 2727

Question: Is it possible to apply to more then one graduate program at the same time?
Answer: 

You may apply to more then one graduate program and get acceptance, however you can register to only one program.


Link: https://faq.cc.metu.edu.tr/faq/it-possible-apply-more-then-one-graduate-program-same-time

---

## Entry 2728

Question: Is it possible to start the application process without declaring a valid score received from the English proficiency and ALES/GRE exams?
Answer: 

The application wouldn’t be evaluated.


Link: https://faq.cc.metu.edu.tr/faq/it-possible-start-application-process-without-declaring-valid-score-received-english-proficiency

---

## Entry 2729

Question: My activation process was completed successfully. What can I do for the next step?
Answer: 

You can start your application.


Link: https://faq.cc.metu.edu.tr/faq/my-activation-process-was-completed-successfully-what-can-i-do-next-step

---

## Entry 2730

Question: My application has not been completed yet but I pressed the ‘EXIT’ button. What will happen now?
Answer: 

 You can only quit the program by clicking the "EXIT" button. Your application information will be kept in the program database.


Link: https://faq.cc.metu.edu.tr/faq/my-application-has-not-been-completed-yet-i-pressed-exit-button-what-will-happen-now

---

## Entry 2731

Question: My Letter of Intention is longer than 2400 characters. What can I do?
Answer: 

If letter of intention is longer than 2400 characters, you can attach the letter of intention to the application form when giving it to the applied institute.


Link: https://faq.cc.metu.edu.tr/faq/my-letter-intention-longer-2400-characters-what-can-i-do

---

## Entry 2732

Question: Program that I want to apply does not require the letter of recommendation. How can I proceed?
Answer: 

You can check "Institute does not require recomendation letter."  in the ‘Letter of Recommendation’ page.


Link: https://faq.cc.metu.edu.tr/faq/program-i-want-apply-does-not-require-letter-recommendation-how-can-i-proceed

---

## Entry 2733

Question: The degree of the program information I want to apply is not in the list. What can I do?
Answer: 

 If the degree of the program information you want to apply is not in the list, you must consult the related program.


Link: https://faq.cc.metu.edu.tr/faq/degree-program-information-i-want-apply-not-list-what-can-i-do

---

## Entry 2734

Question: The institution I want to apply is not in the list. What can I do?
Answer: 

If the institution you are applying is not in the list, the programs of that institution are NOT open for applications. You may contact to the institution for further information.


Link: https://faq.cc.metu.edu.tr/faq/institution-i-want-apply-not-list-what-can-i-do

---

## Entry 2735

Question: The program information I want to apply was not listed. What can I do?
Answer: 

If the program information you want to apply was not listed, you must consult the related institute of the program.


Link: https://faq.cc.metu.edu.tr/faq/program-information-i-want-apply-was-not-listed-what-can-i-do

---

## Entry 2736

Question: What can be done if the activation mail does not arrive?
Answer: 

To get a new activation mail, "'Send Activation " button must be clicked and the required information must be filled in. The activation link provided for you will be e-mailed to you.


Link: https://faq.cc.metu.edu.tr/faq/what-can-be-done-if-activation-mail-does-not-arrive

---

## Entry 2737

Question: What can I enter into the "Intendend Area" boxes?
Answer: 

Intendend Area of Research or Specialization. List them in order of your preferences. To see instructions you may contact to the related institution web page.


Link: https://faq.cc.metu.edu.tr/faq/what-can-i-enter-intendend-area-boxes

---

## Entry 2738

Question: What should I consider in the letter of intention?
Answer: 

Consider the points your background and goals in graduate study ; instructions


Link: https://faq.cc.metu.edu.tr/faq/what-should-i-consider-letter-intention

---

## Entry 2739

Question: How can I apply to the METU Survey Service?
Answer: 

If you are a METU personnel, you can access the page, https://anket.metu.edu.tr/admin and by entering your user code and password, start to use the service without any further applications.


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-apply-metu-survey-service

---

## Entry 2740

Question: Can I form anonymous (whose attendants are not known) and non-anonymous (whose attendants are known), or open to all/specific category surveys by using the METU Survey Service?
Answer: 

While creating a survey, you can choose among various accessibility options according to your purpose. METUSurvey allows forming anonymous, nonanonymous, open to all or restricted access surveys. You can access these options by using Participant Settings option on the Survey Settings menu.


Link: https://faq.cc.metu.edu.tr/faq/can-i-form-anonymous-whose-attendants-are-not-known-and-non-anonymous-whose-attendants-are-known

---

## Entry 2741

Question: Can I modify a survey after activation?
Answer: 

To give access to a survey you need to activate it first. In an activated survey, you can only change the code/title/content of the questions, name/explanation for question groups, contents of the answer options and the name/explanation of the survey. You need to deactivate the survey if you want to add or delete questions, question groups, sub-questions and to change their codes.


Link: https://faq.cc.metu.edu.tr/faq/can-i-modify-survey-after-activation

---

## Entry 2742

Question: Can I test the surveys before publication?
Answer: 

By clicking on the "Preview Survey" button in the admin panel, you can preview and test your surveys.


Link: https://faq.cc.metu.edu.tr/faq/can-i-test-surveys-publication

---

## Entry 2743

Question: How can I access METU Survey Service?
Answer: 

By using the same user name and password that you use at METU central servers, you can enter the site, https://anket.metu.edu.tr/admin. The operations like creating and publishing surveys, arranging the participant information, showing the responses etc. are all done on this site.


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-access-metu-survey-service

---

## Entry 2744

Question: How can I create a survey using METU Survey Service?
Answer: 

After logging in, click on "List surveys" icon. Then, by clicking on "Create a new survey" button, you can create ,copy or upload a survey.


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-create-survey-using-metu-survey-service

---

## Entry 2745

Question: How can I get information on LimeSurvey software?
Answer: 

To access the Limesurvey software help and documentation page, see this link.
You can also access LimeSurvey support forums by following link. There, you will find the forums organized according to their subjects.
For the administration interface demo, follow the link (entering user name: demo, password: test).


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-get-information-limesurvey-software

---

## Entry 2746

Question: How can I see the responses to my surveys?
Answer: 

Using the "Responses" option on the "Survey menu", you can review all the complete and incomplete responses. When your survey expires or when you want to withdraw it, you must "stop" it.


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-see-responses-my-surveys

---

## Entry 2747

Question: What is an access token?
Answer: 

Access tokens are some kind of passwords used for participants to access surveys. These passwords are composed of a number of characters which can be either manually or automatically generated. Once the survey is set as restricted access, these access tokens are sent to the e-mail addresses of the invited attendants. In this way, only those who are invited can access the survey and answer the questions.


Link: https://faq.cc.metu.edu.tr/faq/what-access-token

---

## Entry 2748

Question: Where can I direct my questions and problems regarding METU Survey Service?
Answer: 

You can send your questions, comments and suggestions via e-mail to wwwsurvymetu.edu.tr.


Link: https://faq.cc.metu.edu.tr/faq/where-can-i-direct-my-questions-and-problems-regarding-metu-survey-service

---

## Entry 2749

Question: Who can use METU Survey Service?
Answer: 

All presently employed METU personnel and graduate students.


Link: https://faq.cc.metu.edu.tr/faq/who-can-use-metu-survey-service

---

## Entry 2750

Question: What should I do for creating a blog with my ODTÜ username?
Answer: 

ODTÜ Blog Service allows creating blog and/or personal pages using the accounts defined on the central servers. There is no need for additional registration to this service. You can just log in using the form on the home page and you are done.
The address you can access your blog and/or personal page is like http://blog.metu.edu.tr/{your user code}. This address will be created automatically after your first login.
ODTÜ Blog Service,
Makes it easier to produce personal web pages or blogs without any technical knowledge about web page building
Allows the creation of personal or corporate web pages with respect to the status of your user code.
Allows multilingual blogs or pages to be created
Let you receive comments on your blog posts
Enables using themes prepared in accordance with METU Corporate Identity Standards
Lets you choose from a range of modern themes for your personal pages and/or blogs
Allows domain mapping to make your blog/corporate page accessible in the form of {your user code}.metu.edu.tr on demand.
Users that want to use the METU Blog Service should take METU Blog Service Usage Policy in consideration. The blogs will be deleted after the user codes are deleted from the central servers.
You can access Blog Service Tutorial Videos page from https://blog.metu.edu.tr/en/tutorials/ .
You can use our Contact Form to send us your questions and comments regarding the METU Blog Service.


Link: https://faq.cc.metu.edu.tr/faq/what-should-i-do-creating-blog-my-odtu-username

---

## Entry 2751

Question: How could I find the location of a building or classroom located on ODTÜ?
Answer: 

You can find the location of a building or a classroom on the map through the ODTÜ Interactive Map Service.
You can access the map service via https://map.metu.edu.tr/ address.


Link: https://faq.cc.metu.edu.tr/faq/how-could-i-find-location-building-or-classroom-located-odtu

---

## Entry 2752

Question: Can I Install Applications in PC Rooms?
Answer: 

PC Rooms which are operated by Computer Center, serve the entire university, and the software purchased with the campus license agreement is installed on the computers. Licensed software at https://faq.cc.metu.edu.tr/faq/what-list-software-available-pc-rooms can be used in PC rooms.
Users who log in to computers in PC rooms have a restricted user profile and cannot install programs. Some programs that do not require administrator permission can run on these PCs if there is a portable feature.
Application installation requested by restricted users in public computer labs is not possible due to security, license and compatibility reasons. This type of application installation involves the following risks:
Security Risk: PC rooms are environments that many different users can access and need to be secure. If any user changes an application in the computer lab or installs malware, all of our users may be affected. This can compromise the integrity and security of PC rooms.License and Legal Responsibilities: An application can be installed in a public computer room if it is purchased with a campus license agreement. Failure of applications to meet these requirements may result in license violation and therefore legal problems.Data Loss Risk: There is a risk of data loss during application installation. The security and integrity of the data inside the computers used in the PC rooms is always a priority.Compatibility Issues: The installed application may be incompatible with other applications inside the PC, which may affect the efficiency of the computers.


Link: https://faq.cc.metu.edu.tr/faq/can-i-install-applications-pc-rooms

---

## Entry 2753

Question: How can I access the computers in the PC rooms from off campus?
Answer: 

Our students can access the computers in our PC rooms remotely to use licensed software. You can follow the below steps to connect to the PC room computers and access licensed software.
Considering that your access may be interrupted due to possible network and electrical problems / outages, it is important to save your work files on the J: drive of the computer regularly and copy and paste them to your own computer.
If you leave your session idle for 15 minutes, you will be automatically logged out. For this reason, when your work is finished, you need to transfer your files to your computer and log off.
In order to connect to the PC room computers
You need to connect to VPN first if you are not connected to the campus network. Detailed information is available from http://faq.cc.metu.edu.tr/groups/vpn-service where you can access the instructions to install the appropriate version for your operating system. VPN is not required for in campus connections.
The Remote Desktop Client application required for access is installed on Windows computers. Students using MAC OS should install the Microsoft Remote Desktop application at https://apps.apple.com/us/app/microsoft-remote-desktop/id1295203466?mt=12.
Visit https://pcrooms.cc.metu.edu.tr and login with your METU user code - password. A list of PC rooms ready for connection will be displayed.
Choose one of the PC rooms. A list of PCs that are available will be displayed. Then click the Request link of a computer.
After selecting the computer, press the Download & run the file to connect button. You will have 5 minutes to connect to the computer.
Open the location of the downloaded connect.rdp file on your computer and double click the file and run it.
Press the CONNECT and YES buttons on the warning messages that may appear on the screen.

You can log in to the PC room computer by entering your METU password on the Windows login screen that will come up after a while. If your user code is not automatically typed in, you need to type it, too.

If you get an "authentication error" error at this stage, double click the connect.rdp file again, check the keyboard layout in the lower right part of the login screen and type your usercode - password again.
If your 5-minute connection time has expired, you may receive a message that your connection time has expired. In this case, you have to make a new request.
You can see the list of available software from the Program Shortcuts folder on the desktop.

When your work is finished, you can log off with the Log off button in the Windows Start menu.

If you leave your session open idle for 15 minutes, you will be automatically logged out. For this reason, when your work is finished, you need to transfer your files to your computer and log off.
You can submit your opinions and suggestions about our application and any problems you encounter via support form at https://itsupport.metu.edu.tr.


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-access-computers-pc-rooms-campus

---

## Entry 2754

Question: How can I reach the PC Rooms Map?
Answer: 


PC Rooms

1. Social Sciences2. Dormitory-I3.Dormitory-II (1,2,3)
4. İsa Demiray Dormitory5. Faika Demiray Dormitory 6. Refika Aksoy Dormitory
 

View on  METU Interactive Map   


Link: https://faq.cc.metu.edu.tr/faq/pc-rooms-map

---

## Entry 2755

Question: How can I secure my exams in PC rooms?
Answer: 

Safe Exam Browser is a web browser environment to carry out e-assessments safely. The software turns any computer temporarily into a secure workstation. It controls access to resources like system functions, other websites and applications and prevents unauthorized resources being used during an exam. For the features available in this software, you can visit SEB web site.
This software is available in PC Rooms operated by Computer Center for IS100 online exams. For more information on installing and configuring the software, please visit https://faq.cc.metu.edu.tr/faq/how-can-i-install-safe-exam-browser-computers-my-pc-room


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-secure-my-exams-pc-rooms

---

## Entry 2756

Question: I cannot login to computers in PC rooms with my user code. What should I do?
Answer: 

If you cannot login to the computers in the computer rooms operated by Computer Center:
1. First, please try to login https://useraccount.metu.edu.tr with your usercode and password. If you cannot login either, please follow the instructions on http://faq.cc.metu.edu.tr/faq/i-forgot-my-password-where-can-i-apply to obtain a new password.2. Please check the language icon on the lower right corner of the screen. If it is something other than TUR, then the keyboard layout is different than it is seen. Select TUR in the available options and try entering your password again.
If you can login to the computers and get logged out a minute later:
1. You might be prohibited to use the computers due to a violation of PC Room Use Regulations. Please contact with the IT Support Team via https://itsupport.metu.edu.tr/
2. There might be a temporary malfunction record of the computer you are using. Please try to login to another computer.


Link: https://faq.cc.metu.edu.tr/faq/i-cannot-login-computers-pc-rooms-my-user-code-what-should-i-do

---

## Entry 2757

Question: What are PC Rooms Regulations? (In Turkish)
Answer: 

Please visit http://bidb.metu.edu.tr/en/policies-and-rules for PC Rooms Regulations.


Link: https://faq.cc.metu.edu.tr/faq/pc-rooms-regulations-turkish

---

## Entry 2758

Question: What are the duties of PC Room Supervisors?
Answer: 

The PC Rooms of the Computer Center are run by PC Room Supervisors within the working hours. Outside the official working hours, the Student Lab Assistants perform the management of the Rooms. The staff is answerable to the User Support Group of Computer Center and must certainly abide by the following rules and regulations of Computer Center PC Rooms.
PC Room Supervisors and Student Lab Assistants:
The PC Room Supervisors' main task is to provide the availability of the PC Rooms for the users within the scheduled working periods (other than the times allocated for PC maintenance, cleaning of the rooms etc.) as specified by Computer Center.
The PC Room Supervisors must certainly abide by the Rules and Regulations of PC Rooms that are determined by Computer Center. The PC Room Supervisors should be careful and cautious about the fact that students are observing the CC regulations as well. Included in the tasks of the PC Room Supervisors are giving prudent and reasonable warnings to improper use of facilities and implementing the required penalties against the violation of the rules of PC Rooms.
The PC Room Supervisors are responsible from the handling of a silent and convenient studying environment as well as the maintaining the continuity of such quality PC Room service for our users.
Each PC Room Supervisor should behave politely, and they should establish a mutually respectful relationship with the users. The PC Room Supervisors should avoid being engaged with overt, verbal, gestural hostilities. In case of a disagreement or dispute with a user during the shift, The PC Room Supervisors should instantly inform the CC staff about the incident, if the incident happened during the working hours. If the incident did not happen during the working hours, the PC Room Supervisors should inform the information office of the dormitory about the matter.
In case the lights go out, the PC Room Supervisors should inform the users that UPS may fail as well. The PC Room Supervisors should then shut down all the PCs within 5 minutes.
In case of a fire, the first task of the PC Room Supervisors is to be ready to use the fire extinguishers that are available in PC Rooms and call the Office of the Watchman ("Nöbetçi Amirliği (Phone:2113,2114)").
The PC Room Supervisors are to report the technical problems that arise during their shift to CC staff by using form for reporting technical problem ("Arıza Bildirim Formu"), which is available on the lab program.
The PC Room Supervisors are to watch and take care of the registered movable items of the PC Rooms. In case of damage to any of the properties, the PC Room Supervisors must report it instantly to Computer Center.
 

Link: https://faq.cc.metu.edu.tr/faq/duties-pc-room-supervisors

---

## Entry 2759

Question: What are the PC Rooms Hardware Configurations?
Answer: 

LOCATION 
NUM. OF PCs
CPU 
RAM 
DATA SHOW 
Humanities PC Room
32 
AMD Phenom IIX4 3.2 GHz
4 GB 
Available 
Dormitory 1 PC Room 
10
Intel core i5-6500 3.5 Ghz
8 GB 
 
Dormitory 2 PC Room 2 
25
Intel Core i7-10700 
8 GB
 
Dormitory 2 PC Room 3 
40
Intel core i5-6500 3.5 Ghz
8 GB
Available
Faika Demiray PC Room
10
Intel core i5-6500 3.5 Ghz
8 GB 
 
İsa Demiray PC Room 
10
Intel core i5-6500 3.5 Ghz
8 GB 
 
Refika Aksoy PC Room 
10
Intel core i5-6500 3.5 Ghz
8 GB 
 
 
Last update: 2014-04-04 09:16:24


Link: https://faq.cc.metu.edu.tr/faq/pc-rooms-hardware-configuration

---

## Entry 2760

Question: What are the PC Rooms Working Hours?
Answer: 

All labs are available for public use during regular working hours except for the indicated times.
Location
Hours
Days
Cleaning and Infrastructure Maintenance Hours
Humanities PC Room

09:00 - 17:00Course Schedules are announced at the PC Room.

Monday - Friday
CleaningTuesday 09:00 - 10:00
Dormitory 1 PC Room
09:00 - 06:00

Everyday during classes carry on
09:00 - 17:00 during semester breaks

EverydayCleaning 07:00-09:00
Dormitory 2 PC Room - 2
09:00 - 06:00

Everyday during classes carry on
09:00 - 17:00 during semester breaks

EverydayCleaning 07:00-09:00
Dormitory 2 PC Room - 3
This room is reserved fortraining and seminars
Everyday
EverydayCleaning 07:00-09:00
Isa Demiray Dormitory PC Room
09:00 - 01:00
Everyday during classes carry on
EverydayCleaning 07:00-09:00
Faika Demiray Dormitory PC Room
09:00 - 01:00
Everyday during classes carry on
EverydayCleaning 07:00-09:00
Refika Aksoy Dormitory PC Room
09:00 - 01:00
Everyday during classes carry on
EverydayCleaning 07:00-09:00
 
 
 
 
During summer, the PC rooms are open if the dormitory building is open.


Link: https://faq.cc.metu.edu.tr/faq/pc-rooms-working-hours

---

## Entry 2761

Question: What is the list of Software Available in PC Rooms?
Answer: 

PC rooms operated by the Computer Center serve to all users of the university and the centrally licensed software are available on the PCs, along with Windows 10.
7-Zip File Manager
ABBYY FineReader 10 Corporate Edition
Acrobat Reader DC
Adobe CC
ANSYS AIM 17.2
ArcGlobe 10
ArcMap 10
ArcScene 10
AutoCAD 2011 - English
AutoCAD Civil 3D 2011 Imperial
Autodesk 3ds Max Design 2011 64-bit
Autodesk Design Review
Autodesk Inventor Prof 2011
Autodesk Revit Architecture 2011 x64
Autodesk Vault 2011
Bitvise SSH Client
COMSOL Multiphysics 5.6
Dev-C++
DWG TrueView 2011
Dytran 2018.0
Ecotect Analysis 2011
EQS 6.3 for Windows
FileZilla Client
Force 2.0
GIMP 2
Google Chrome
IBM SPSS Statistics 28
ImgBurn
Jamovi 1.0.7.0
JMP 12
KompoZer
LibreOffice 6.0
Marc Mentat 2017.1.0
Mathcad 15
MATLAB R2021b
Microsoft Office 2016
Mozilla Firefox
MPC-HC x64
MSC Apex Fossa
MSC Nastran 2018.1
MSC Sinda 2017.1
Nvu
NX 11.0
Patran 2018 (Classic)
Picasa 3
PuTTy
RStudio
R x64 3.5.0
Safe Exam Browser
Simufact Forming 15.0
Wolfram Mathematica 12.3
Workbench 19.2
 

Link: https://faq.cc.metu.edu.tr/faq/what-list-software-available-pc-rooms

---

## Entry 2762

Question: Which PC Rooms are available for course registrations?
Answer: 











All labs are available for public use during regular working hours except for the indicated times.
Location
Hours
Days
Cleaning and InfrastructureMaintenance Hours
Humanities PC Room

09:00 - 17:00Course Schedules are announced at the PC Room.

Monday - Friday
CleaningTuesday 09:00 - 10:00
Dormitory 1 PC Room
09:00 - 06:00

Everyday during classes carry on
Closed during semester breaks

EverydayCleaning 07:00-09:00
Dormitory 2 PC Room - 2
09:00 - 06:00

Everyday during classes carry on
09:00 - 17:00 during semester breaks

EverydayCleaning 07:00-09:00
Dormitory 2 PC Room - 3
This room is reserved fortraining and seminars
During planned training and seminars
EverydayCleaning 07:00-09:00
Isa Demiray Dormitory PC Room
09:00 - 01:00
Everyday during classes carry on
EverydayCleaning 07:00-09:00
Faika Demiray Dormitory PC Room
09:00 - 01:00
Everyday during classes carry on
EverydayCleaning 07:00-09:00
Refika Aksoy Dormitory PC Room
09:00 - 01:00
Everyday during classes carry on
EverydayCleaning 07:00-09:00
 
 
 
 
During summer, the PC rooms are open if the dormitory building is open.












Link: https://faq.cc.metu.edu.tr/faq/which-pc-rooms-are-available-course-registrations

---

## Entry 2763

Question: How can I update the operating system of my computer?
Answer: 

If you are using Windows 11 operating system, select; Select the Start button, then click on Settings.Update & Security. Click on Update & Security.Windows Update. Select Check for updates to see if your PC can run Windows 11, or if the upgrade is ready for your PC.
If you are using Windows 10 operating system, select; Start button, then select Settings > Update & Security > Windows Update >, and then select Check for updates. Check for updates.
If you are using Windows 7 operating system, select;
_x0095_  Start > All Programs > Windows Update
or;
_x0095_  Control Panel > System and Security > Windows Update
Update for Linux Operating Systems Distributions:
If you are using Linux based operating systems, depending on the type of the operating system you can update from different sites.
_x0095_  RedHat: Type up2date command to connect to the update site.
_x0095_  Mandrake: Type MandrakeUpdate command to connect to the update site.
_x0095_  Debian: Start apt-setup program, if it is not installed, install it with apt-get. Using this program select the access method (ftp or http) to Debian package archive. Then choose the archive site from the list. After these steps:
apt-get update: Updates the package list.
apt-get upgrade: Installs the latest version of the available packages.


Link: https://faq.cc.metu.edu.tr/faq/how-can-i-update-operating-system-my-computer

---

## Entry 2764

Question: my e-signature certificate is expired, what should i do?
Answer: 

If your e-signature certificate is about to expire or is already expired, please visit https://eimza.metu.edu.tr and apply for a renewal (yenileme) for your certificate. Then, the related procedures will be started.
Please wait for the e-mail from KamuSM and Computer Center for further instructions.










Link: https://faq.cc.metu.edu.tr/faq/my-e-signature-certificate-expired-what-should-i-do

---

## Entry 2765

Question: What can I do to make my Apple MAC computer more secure?
Answer: 

APPLE MAC SECURITY PRECAUTIONS
Your Apple MAC computer can get the threats from two sources:
1. The Internet 2. Direct Access / Physical Access (if you leave your computer unattended or without taking the necessary precautions)
What can you do to increase your MAC’s security features?
Basically, you will do all the configuration by clicking the Apple icon on the left top corner and choosing the System Preferences option.

1. Using a standard user: When setting up a new operating system, the user that is defined is an administrator type user. Admin users are entitled to make any changes on the computer. It’s a safer practice to use your computer with standard user rather than an administrative user. (Apple>System Preferences> User and Groups option you can change the user type to standard and renew the password.)

2. Secure Password Policy:
Do not choose your password from easily guessable passwords like your name, birthday, phone number or from ones that can be obtained from dictionary or brute force attacks. Secure password policy can be summarized in its simplest form as: A phrase containing at least 8 characters including uppercase, lower case letters, special characters (!, #, $, +, &) and digits. 
3. Disable Automatic login Option:
Disable automatic login option (login without entering a password to the computer).  (Apple > System Preferences > User and Groups >  Login Options; choose automatic login off).

4. Uninstall Flash Player
Flash Player is a software that can contain many security vulnerabilities. If you do not use the software at all, just uninstall it. If you do use it, then set it to make updates automatically. (Apple > System Preferences)

5. Use a Password Manager:
In the world of today, we use many different passwords for various purposes and of course we have to remember them. We would again like to remind you about the password policy in number 2. Besides, instead of keeping all the passwords in your memory, you can keep only one password in mind which is the password manager program’s password and keep the all the other passwords in the manager program safely. (Programs like Key Chain, 1 Password, Keeper that you can download from App Store)
6. Encrypt the files in your disk with File Vault:
If there are valuable files on your MAC computer, you can encrypt your files towards unwanted access. (Apple > System Preferences > Security&Privacy > FileVault tab and turn it on.)

7. Review your Spotlight Permissions:
Spotlight forwards your searches to Apple and Apple can share your information to third party partners. If you would like your search information to remain private, review your Spotlight options. (Apple > System Preferences > Spotlight > Privacy tab, you can define exceptions for your information not be forwarded.

8. Location Services
Inspect your applications that you share your location services with, and disable the ones that are unnecessary. (Apple > System Preferences > Security & Privacy > Privacy tab) Do not forget that the “Find My MAC” application works with location services; and if your MAC is lost or stolen you will be able find your device with the help of this feature. It’s a better idea to use location services with appropriate permissions. 

9. Software Updates
Follow the software updates frequently, and even set it to an automatic version. (Apple > System Preferences > App Store tab there is an option to automatically download and set up the updates).

10. Use Your Screen Saver Efficiently
Do not leave your computer unattended. For securing the computer and the data on it, define a screensaver that will activate after a short time the computer stays idle and will be disabled only by entering your password. (Apple > System Preferences > Desktop & Screen Saver).
11. Activate your Firewall
Activate your firewall and enable it in stateful mode, which means, no one will be able to make a connection to your computer unless you start the connection. (Apple > System Preferences > Security&Privacy > Firewall tab; activate with Firewall on; click Firewall options > Block all incoming connections option will enable your firewall to become a stateful firewall.)


12. Sharing
Control your Sharing. Avoid unnecessary sharing and disable them. (Apple > System Preferences > Sharing) Use this tab to control each service and disable the ones that are unnecessarily enabled. 

13. Define a Firmware Password:
You are encrypting the data on your computer with FileVault but this still does not guarantee a malicious person to boot your computer with a USB stick and erase all the data or install operating system from scratch, in case your computer is stolen or lost. When you define a firmware password, unlike in the case of PCs, firmware password will be asked only if you try to boot the system with unconventional ways. To define firmware password: When booting up the computer, press Cmd+R when the Apple logo appears; then on the screen that appears select Utilitiesà Firmware Password Utility. Please be careful defining this password, since if you forget it, you may need to visit the Apple Authorized Service.
14. Two Step Authentication
If you define two step authentication on your MAC, you will add an additional layer of security. (The second step is a verification code that comes to your telephone) You can find information on Apple’s web page about two step authentication.
15. Guest User
Defining a guest user: If you have enabled FileVault, you can use guest user and login the computer without password; use just Safari and all the data generated through the guest login is erased after the user logs out. Enabling the guest user on the computer enables the computer to be relocated after it’s lost or stolen. (Apple > System Preferences > User & Groups option).

16. Find My MAC!
Activate Find My MAC to relocate your computer if it is stolen or lost. (Apple > System Preferences > iCloud > Find My MAC must be selected.)
17. Third Party Antivirus Software
You can use third party antivirus software to determine malicious code on your MAC. For example, you can use the free version of BitDefender (Can we downloaded from App Store).
18. Use VPN
If you utilize open wireless networks a lot (like airports, coffee shops, libraries etc) you can take advantage of Virtual Private Networks (VPNs) to secure your traffic over the Internet. (Apple > System Preferences > Network, in the box on the left side, click “+” to set up VPN service.) METU offers a VPN service to the users but through this service you can access only local services and network of METU. Visit page https://faq.cc.metu.edu.tr/faq/how-can-i-use-metu-vpn-service-mac-os-x-installed-devices to setup VPN service of METU.

19. Use Legal Software
Do not install illegal software. Do not use Warez. If you use software from Warez, you enable unwanted, malicious codes on your computer. To increase your security, install software only from App Store or identified developers. (Apple > System Preferences > Security & Privacy > General tab, choose Allow apps downloaded in a secure way).
20. Backup Your Data
You should always backup your valuable data against theft, loss, physical damage on disc etc. (Apple > System Preferences > Time Machine).

21. use eduroam SSID for wireless in METU
There are 2 SSIDs for wireless network in METU Campus, eduroam and ng2k. ng2k is an open wireless network that works with MAC address authentication. On the other hand eduroam is secure wireless network working on RADIUS based 8021.x security standard. Furthermore if you setup eduroam on your device, you can wireless network in any institution that is a member of the eduroam infrastructure. You can visit http://eduroam.metu.edu.tr to get information about setting up eduroam SSID on your computer.
References: 
1.     http://www.macworld.co.uk/feature/mac/22-ultimate-tricks-improve-mac-security-best-tips-3643100/
2.     https://www.intego.com/mac-security-blog/15-mac-hardening-security-tips-to-protect-your-privacy/


Link: https://faq.cc.metu.edu.tr/faq/what-can-i-do-make-my-apple-mac-computer-more-secure

---

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

