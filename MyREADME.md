#HS029 Odoo development

##Directories
### **libraries**
Downloaded codes, e.g. download from github
### **myaddons**
Developed by myself

##How to run
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8

**Run without specify database, this is normal case. If ran specified database, need to edit odoorc to remove db_name**

./odoo-bin --config=odoo.conf

./odoo-bin --addons-path=addons,myaddons --db_user=shuai --db_password=Zs775825 --db_port=5432 --load-language zh_CN --logfile odoo.log -s -c odoorc

./odoo-bin -i base --addons-path=addons --db_user=shuai --db_password=Zs775825 --db_port=5432 --load-language zh_CN --logfile odoo.log -s -c odoorc 

./odoo-bin -i base --addons-path=addons,myaddons,gooderp_addons --db_user=shuai --db_password=Zs775825 --db_port=5432 --load-language zh_CN --logfile odoo.log -s -c odoorc

**Run with specific database**

./odoo-bin --database=odoo12 -i base --addons-path=addons --db_user=shuai --db_password=Zs775825 --db_port=5432 --load-language zh_CN --logfile odoo.log -s -c odoorc

**below is in test mode**

./odoo-bin --database=odoo -i base --addons-path=addons --db_user=shuai --db_password=shuai --db_port=8432 -l zh_CN --dev all -s -c odoorc 

**PyCharm Configure

/Users/shuai/github/hserp/odoo.bak/odoo-bin -c odoo.conf --dev=all
