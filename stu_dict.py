
slang_dict={"大冤种":"东北方言演变而来，用于形容做了傻事的人或倒霉蛋",
            "小镇做题家":"描绘了一群来自小城镇，专注于学习但可能视野有限的年轻人。"}

slang_dict["您幸福了"]="源自东北地区的一种祝福语，幸福与辛苦谐音，传达了积极的生活态度"

query_dict = input("请输入您要查询的流行语：")

if query_dict in(slang_dict):
    print("您查询的"+query_dict+"含义如下：")
    print(slang_dict[query_dict])
else:
    print("您查询的流行语在本词典没有收录")
    print("本词典收录了"+str(len(slang_dict))+"条")



