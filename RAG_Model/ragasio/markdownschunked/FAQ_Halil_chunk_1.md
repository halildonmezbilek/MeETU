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