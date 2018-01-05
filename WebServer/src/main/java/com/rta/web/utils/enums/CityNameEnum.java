package com.rta.web.utils.enums;

/**
 * @author lkc
 * @date 18-1-5 下午7:15
 */
public enum  CityNameEnum {
    XI_AN("xa","西安市"),
    BEI_JING("bj","北京市"),
    SHEN_ZHEN("sz","深圳市"),
    SHANG_HAI("sh","上海市");
    String abbr;
    String name;

    CityNameEnum(String abbr, String name) {
        this.abbr = abbr;
        this.name = name;
    }

    public String getAbbr() {
        return abbr;
    }

    public String getName() {
        return name;
    }

    public static CityNameEnum getByAbbr(String abbr){
        for (CityNameEnum cityNameEnum : CityNameEnum.values()){
            if (cityNameEnum.abbr.equals(abbr)){
                return cityNameEnum;
            }
        }
        return null;

    }
}
