import os
os.system("nmap -script http-sitemap-generator -script http-php-version -script http-sql-injection -script ssl-ccs-injection -script http-csrf testphp.vulnweb.com 34.231.173.234 -oX ozanNmap.xml")

