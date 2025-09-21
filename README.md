![Edge AI Module Mk-4](images/edge_ai_module.jpg)

# Edge AI Module
### By [Matthew Thomas Beck](https://www.linkedin.com/in/matthewthomasbeck/)

Special thanks to [Omar Ferrer](https://www.linkedin.com/in/omar-ferrer-0bb6355a/) for his help

Click [here](https://www.matthewthomasbeck.com/pages/edge_ai_module.html) for the story behind the build

Please consider: if you like it, **star it!**

## Tech Stack
- **Language:** *Python*
- **Libraries:** *threading, queue, time, os, socket, logging, collections.deque, subprocess, signal, sys, random, numpy, opencv-python, openvino, smbus, RPi.GPIO, pigpio, pyserial*
- **Toolkits:** *OpenVino*

## Basic Information

If you want a cheap way to rapidly-prototype a variety of robots, this module may be for you! It will take a bit of work to set up, but you are guaranteed to save much more money as opposed to buying a something like a Jetson board

## **(WIP)** Build For Yourself!

1. Ensure you have these tools:

| **Tools** |
| ----------- |
| 3D Printer (PLA and TPU) |
| Soldering Iron (rosin-core solder) |
| Wire Strippers |
| Lighter/Heat Gun |
| Hex Keys (M2/M3) |
| Good Lighting |

2. Purchase the electronics/components as follows:

| **Components** | **(remember, do your own research to save money)** |
| ----------- | ----------- |
| x1 Raspberry Pi 4B | [Amazon](https://www.amazon.com/Raspberry-Pi-Computer-Suitable-Workstation/dp/B0899VXM8F/ref=sr_1_4?crid=319NNK3ODD0NN&dib=eyJ2IjoiMSJ9.mP4drOfyakW9P2E6ytjWi-0Eme9cX9WdEfmoOEAEkYbYx13g9nuKnUr6p98SCxu5L1h1EbkmEHVa6sgyYU8pgBpOg6iwMPjMt_5Tg3FRT7L4ne2vxyfQoR_kU-Fyo7CqR1DIal6K5glha86oKB9U9lTIye1AbgbhAlkPRx8At6GX2OMOEXepvjEcIpPv4hA-OciEixYFsy9O8hMdVqBXNeRZk47ogtanVdMHIXglfVg.mV1nhwpM8rWXMqMP0Ydi-EwvBshs8fAqD0lud5HHG4Y&dib_tag=se&keywords=raspberry+pi+4B&qid=1758419926&sprefix=raspberry+pi+4%2Caps%2C180&sr=8-4) |
| x1 Intel NCS2 | [eBay](https://www.ebay.com/sch/i.html?_nkw=Intel+NCS2+TPU&_sacat=0&_from=R40&_trksid=p2334524.m570.l1313&LH_TitleDesc=0&_odkw=ncs2&_osacat=0) |
| x1 Pololu 12-Channel Maestro | [Amazon](https://www.amazon.com/Mini-Maestro-12-channel-Servo-Controller/dp/B007MX0ED6/ref=sr_1_1?crid=1YLB6H4XC6ALM&dib=eyJ2IjoiMSJ9.yr_Rj_G2lc9KWCMBxKOMIQ.un9qQKBEiN--f38FXuq5ORUOvyR57Tfq9IA8dszhSGE&dib_tag=se&keywords=pololu+maestro+12+channel&qid=1758420024&sprefix=pololu+maestro+12+channel%2Caps%2C181&sr=8-1) |
| x1 HiLetgo GY-521 MPU-6050 | [AliExpress](https://www.aliexpress.us/item/3256806865414323.html?spm=a2g0o.productlist.main.11.78d56jiw6jiwvu&aem_p4p_detail=2025092018533812904255132669920001907890&algo_pvid=75101ec7-3a77-4807-9601-ee3e168e6be2&algo_exp_id=75101ec7-3a77-4807-9601-ee3e168e6be2-10&pdp_ext_f=%7B%22order%22%3A%224%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21USD%212.25%210.99%21%21%2115.95%217.01%21%402101c59817584196186736820eb660%2112000039234877353%21sea%21US%210%21ABX%211%210%21n_tag%3A-29910%3Bd%3A61b1bf00%3Bm03_new_user%3A-29895%3BpisId%3A5000000174221210&curPageLogUid=gpkoMCMrUWnD&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005007051729075%7C_p_origin_prod%3A&search_p4p_id=2025092018533812904255132669920001907890_10) |
| x1 Pi Camera Module 3 (75°) | [AdaFruit](https://www.adafruit.com/product/5657) |
| x1 RadioLink T8S 8 Channels | [Amazon](https://www.amazon.com/Radiolink-Channels-Transmitter-Controller-Rechargeable/dp/B09BTSJN7P/ref=sr_1_6_pp?crid=3HAHHSJXUICJR&dib=eyJ2IjoiMSJ9.hK57psznX9fBBourL6e2v0FcyoQvn5F_DnarlcdyEOC53AuSif3K_v1Xp4h1Hkv42vy_VI2PkR_XlYTYj4R6crJ54HP-4CLHxLspdfdMTuV0o8A6eTLOMhQo88pFu-V9mLpLQ2t-oH5ZnDv100daJI14OBJhjZ4nb2S6FQJQaPfVAmGHQPxfNewZh5BkYYfpYy-LhZcrGbdyyxn-s_dnM0D8gwfFj7Gb5AkeVbaJND9LEvS5tCnEJiY6gPojZPlBFcUEsyHUwtILS9aOQ1FI2f3KE2Uf7fNBpwyh_qHBf1k.vf2e0eh0uRRIoEySAnbTJaIC0bpvfnDS9aSX8X6vnUk&dib_tag=se&keywords=radiolink%2Breceiver&qid=1758420216&sprefix=radiolink%2B%2Caps%2C189&sr=8-6&th=1) |
| x1 3.3/5.0V Fan | [AliExpress](https://www.aliexpress.us/item/3256809007098220.html?spm=a2g0o.productlist.main.5.51a8RdCSRdCSgS&algo_pvid=cb998540-a52e-4e77-b065-9a76347e24e2&algo_exp_id=cb998540-a52e-4e77-b065-9a76347e24e2-4&pdp_ext_f=%7B%22order%22%3A%2230%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21USD%2110.55%210.99%21%21%2174.65%216.99%21%402101e7f617584204491512686edad1%2112000048256676817%21sea%21US%210%21ABX%211%210%21n_tag%3A-29910%3Bd%3A61b1bf00%3Bm03_new_user%3A-29895%3BpisId%3A5000000174221210&curPageLogUid=QE6VZrus9GSV&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005009193412972%7C_p_origin_prod%3A) |
| x2 LM2596 Buck Converter | [AliExpress](https://www.aliexpress.us/item/2255800279067821.html?spm=a2g0o.productlist.main.10.20d0WKW8WKW8VU&algo_pvid=66083cd4-f44e-416c-8633-84383f751043&algo_exp_id=66083cd4-f44e-416c-8633-84383f751043-9&pdp_ext_f=%7B%22order%22%3A%2260%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21USD%211.90%210.99%21%21%211.90%210.99%21%402101e7f617584205195188672edad4%2110000001878664730%21sea%21US%210%21ABX%211%210%21n_tag%3A-29910%3Bd%3A61b1bf00%3Bm03_new_user%3A-29895%3BpisId%3A5000000174221210&curPageLogUid=k3UXG3l7ZiKW&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A4000465382573%7C_p_origin_prod%3A) |
| x1 18-Gauge Wire Spool | [Amazon](https://www.amazon.com/BNTECHGO-Silicone-Flexible-Strands-Stranded/dp/B01C5CANVG/ref=sr_1_1_sspa?crid=KVB1VTUHP2QX&keywords=18%2Bawg%2Bwire&qid=1654286009&s=industrial&sprefix=18%2Bawg%2Bwir%2Cindustrial%2C105&sr=1-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyUllBSVdMMDU0NTEmZW5jcnlwdGVkSWQ9QTA0MjgyODUzT1U3REpIQk44WVZVJmVuY3J5cHRlZEFkSWQ9QTAzMjc3MjUzTDAzQ0MyVkhUQ0xBJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ&th=1) |
| x1 F-F 5V Wire Set | [Amazon](https://www.amazon.com/XLX-Breadboard-Soldering-Brushless-Double-end/dp/B07S62XN5M/ref=sxin_17_pa_sp_search_thematic_sspa?content-id=amzn1.sym.5a2f80d8-3686-499a-bbaa-70664bd0de70%3Aamzn1.sym.5a2f80d8-3686-499a-bbaa-70664bd0de70&crid=2LZXPWJ5Y1INN&cv_ct_cx=pin+wires+female+to+female&keywords=pin+wires+female+to+female&pd_rd_i=B07S62XN5M&pd_rd_r=76348b85-1525-4283-866c-155099ecc5a8&pd_rd_w=nAxNY&pd_rd_wg=z3x67&pf_rd_p=5a2f80d8-3686-499a-bbaa-70664bd0de70&pf_rd_r=3TNPC1JQAKRHY7CQMJMH&qid=1758420896&s=industrial&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&sprefix=pin+wires+female+to+female%2Cindustrial%2C130&sr=1-1-6024b2a3-78e4-4fed-8fed-e1613be3bcce-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9zZWFyY2hfdGhlbWF0aWM&psc=1) |
| x1 M3 8mm Screws | [Amazon](https://www.amazon.com/Socket-Screws-Bolts-Thread-100pcs/dp/B07CMQ1SQH/ref=sr_1_3?crid=1LU3IAQCLHKDD&keywords=m3%2Bx%2B8mm&qid=1654294212&sprefix=m3%2Bx%2B4mm%2Caps%2C512&sr=8-3&th=1) |
| x1 Nylon Screw Set | [Amazon](https://www.amazon.com/Lystaii-Standoff-Motherboard-Standoffs-Assortment/dp/B0BYSHZ2TD/ref=sr_1_3?crid=3TQU23QNVS504&dib=eyJ2IjoiMSJ9.2-cdeX5wWVvE79Wr7KgdlPWA4QqroAJ2IenZQVXXSctS4SCYlaDiEaSzuFghuNNo5QnQN98cs20AIsm9xsITnprW7BQ8BT65TbrthLu2pmlZfn3kSk-dqw7Nz42A8s21Qc7K6P74JIXcAz4Rnd_Itjx0njaNLJ-YqKv3HIGu0DaRK4r7NsnOY46bn64YbKAiL80qKsyBwfh7d5DpMHM0JatubFbvQmfJrmKxuyK6O-NEsEMJFQ74fWhtiq0pPqfn770TkMWeJ9ix3SHlD5MJ2kX7-3Zr8kVNqZySrELMs0w.6g3ERWPGb6DGei2Hx6es6DloT0pIaciWRF7L6u_2rzU&dib_tag=se&keywords=m2+nylon+screws&qid=1758421573&s=industrial&sprefix=m2+nylon+screws%2Cindustrial%2C165&sr=1-3) |
| x1 M3 Brass Inserts | [Amazon](https://www.amazon.com/dp/B07LBQRYR3?ref=ppx_yo2ov_dt_b_product_details&th=1) |
| x1 M2 Brass Inserts | [Amazon](https://www.amazon.com/dp/B0DG8R9XFG?ref=ppx_yo2ov_dt_b_product_details&th=1) |
| x1 Heat-Shrink Tubing Set | [AliExpress](https://www.aliexpress.com/ssr/300000512/BundleDeals2?spm=a2g0o.productlist.main.2.4e288u9c8u9c2p&productIds=1005005336957133:12000032659479346&pha_manifest=ssr&_immersiveMode=true&disableNav=YES&sourceName=SEARCHProduct&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005005336957133%7C_p_origin_prod%3A) |
| x1 Zeee 2S Lipo Batteries | [Amazon](https://www.amazon.com/Zeee-Battery-Connector-Airplane-Helicopter/dp/B08GFRT9S9/ref=sr_1_6?crid=1PUOYGY56LFLM&dib=eyJ2IjoiMSJ9.1bk3JfV9Bj-7Nbnmeoh8H5F1mtySRT8rZ9HFf4nj5oTPZ0hTYPI9idRQpKsUS73wlcX5vezivXxFbJF6QRDOnkLocNy9m0Rva6a91xf9pL57Y6vVvtpsds6gaqCJG9Tn77Ipcx6BSa-EE7HNT87kMvgwLYh5zDgcvUsCEgvk8-WTWx9vqfEzV_yqQx5jEP1TXCU3t6xmY_oaX-NGHgCXzry-luujLwsnYUNT8EAZNlxCd52b1shU-4rqgtHZzq8bBno6wzKyX9nogEis89LcSULK1kBHDSyR0IhTTVYblho.OxlMupoaaxbJ9kI5PghW69lt2A1ol1Y1ifR7Bevmrb8&dib_tag=se&keywords=5200mah+100c+lipo+battery&qid=1758422241&sprefix=5200mAh+100C+7.4V+%2Caps%2C230&sr=8-6) |
| x1 USB-C Vertical Male Plug | [AliExpress](https://www.aliexpress.us/item/3256808930024592.html?spm=a2g0o.productlist.main.2.71d531bdaZBwGE&algo_pvid=9e7f8eb6-f21c-4b2a-b77a-c3c9d1dc0cfd&algo_exp_id=9e7f8eb6-f21c-4b2a-b77a-c3c9d1dc0cfd-1&pdp_ext_f=%7B%22order%22%3A%2219%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21USD%211.18%210.99%21%21%218.36%217.05%21%40210318c317584223371023738e6a60%2112000047974998506%21sea%21US%210%21ABX%211%210%21n_tag%3A-29910%3Bd%3Ac73cf665%3Bm03_new_user%3A-29895%3BpisId%3A5000000174221210&curPageLogUid=rKs8H6hAkAH3&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005009116339344%7C_p_origin_prod%3A&_gl=1*x03du9*_gcl_au*MTU1Nzk5NzI0MS4xNzU4NDE5NjA3*_ga*MTg4NDY4ODMzNy4xNzU4NDIwMjU4*_ga_VED1YSGNC7*czE3NTg0MjAyNTckbzEkZzEkdDE3NTg0MjIzNDAkajQzJGwwJGgw) |
| x1 Switch | [AliExpress](https://www.aliexpress.us/item/3256804425729825.html?spm=a2g0o.productlist.main.1.2c74530aMzsNiU&algo_pvid=c0ae865a-cbc4-4f06-ad83-9db647a51254&algo_exp_id=c0ae865a-cbc4-4f06-ad83-9db647a51254-0&pdp_ext_f=%7B%22order%22%3A%222%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21USD%213.74%210.99%21%21%213.74%210.99%21%402101c71a17584224820891793e94ae%2112000029828041967%21sea%21US%210%21ABX%211%210%21n_tag%3A-29910%3Bd%3A61b1bf00%3Bm03_new_user%3A-29895%3BpisId%3A5000000174221210&curPageLogUid=K8ZhKrdJlsYD&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005004612044577%7C_p_origin_prod%3A) |
| x1 XT60H Connector Pairs | [Amazon](https://www.amazon.com/Upgrade-Female-Bullet-Connectors-Battery/dp/B07VRZR5TL/ref=sr_1_2?crid=3N6T3XK812QTD&keywords=XTC+connector&qid=1654285537&sprefix=xtc+connector%2Caps%2C124&sr=8-2) |
| x1 XT60H Adapter Set | [Amazon](https://www.amazon.com/JIECHUN-Adapter-Connector-Battery-Charger/dp/B0BLHGR17L/ref=sr_1_7?crid=2A3AF1IL9H5ZJ&dib=eyJ2IjoiMSJ9.FiDHaGTf8BeWanc3XY2BeNsVi3THvyi52_yFeG9ANy82aE6yB-yXIPb_UmhS4U0qm4SfLqdTkC8lBbh8qriKTjKZ_rDT6i_dDQAttfwQF800WOwEq0W8_Cnak0vBlOD3Y4rcuw6DW3o-E5z9lsiLJnSHpPgJhQbLwph3pKLZmB9Jty_JTan-hugMTHjPXfRMu78_88irz4OexB_eK5GQE7t_Icq2eNSQxxi-wWBz_SOx4wPP7XVa9k16PipXmxj5KkwiJydkHYM_HOcIu66FBAWj4ReLx_4S7O1QKHNUA7k.b7W43x4jTFb7LT6EwLjM2oEC_963RF1pq91qbKkty_4&dib_tag=se&keywords=XTC60+adapter&qid=1758422674&sprefix=xtc60+adapt%2Caps%2C232&sr=8-7) |

3. Print out the 3D components as found in the '3D_parts' folder

4. **(WIP)** Follow this tutorial video here ← (currently making video)

5. Configure OpenVino for Raspberry Pi 4B using 'OpenVino_Setup.txt' (this was VERY hard, take your time)

6. Use the files/functions found in 'utilities' to accelerate development