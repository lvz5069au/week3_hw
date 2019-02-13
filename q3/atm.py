from db.model import Model

def showATM(usr):

    print("|{0:<5}| {1:<10}|".format( "username","balance"))
    print("-" * 40)
    print("|{0:<5}| {1:<10}|".format( usr['name'],  usr['balance']))



def login(userList):
    if len(userList) == 0:
        print("==========  没有任何用户存在！=============")
        return 0
    times = 3
    while times > 0:
        name = input("请输入用户名： ")
        passwd = input("请输入密码： ")
        for usr in userList:
            if name == usr['name'] and passwd == usr['password']:
                id  =  usr['id']
                return id
        print("用户名或密码输入错误,请重新输入...")
        times -= 1
    return 0


if __name__ == '__main__':
    mod = Model("userinfo")
    foo = login(mod.findAll()) ## return an id or zero
    if foo > 0:
        while True:
            print("=" * 12, "ATM自动提款机", "=" * 14)
            print("{0:1} {1:13} {2:15}".format(" ", "1. 查看余额", "2. 存钱"))
            print("{0:1} {1:13} {2:15}".format(" ", "3. 取钱", "4. 退出系统"))
            print("=" * 40)
            key = input("请输入对应选择：")

            if key == "1":
                print("="*12,"账户信息浏览","="*14)
                showATM(mod.find(str(foo)))
                input("按回车键继续：")

            elif key == "2":
                print("=" * 12, "存入现金", "=" * 14)
                bal = mod.select(where=["id = %s"%foo])
                bal[0]['id'] = foo
                bal[0]['balance'] += float(input("请输入要存的金额："))
                mod.update(bal[0])
                input("按回车键继续：")

            elif key == "3":
                print("=" * 12, "请输入要取出的金额", "=" * 14)
                bal = mod.select(where=["id = %s"%foo])
                bal[0]['id'] = foo
                bal[0]["balance"] -= float(input("请输入你要取出的金额："))
                mod.update(bal[0])
                input("按回车键继续：")

            elif key == "4":
                print("=" * 12, "再见", "=" * 14)
                break
            else:
                print("======== 无效的键盘输入！ ==========")
    else:
        print("你输入错误次数过多，再见...")

