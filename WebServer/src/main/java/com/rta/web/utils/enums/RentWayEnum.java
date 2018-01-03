package com.rta.web.utils.enums;

import lombok.Data;

/**
 * @author lkc
 * @date 18-1-3 下午1:28
 */
public enum RentWayEnum {
    // 整租
    ALL(0,"整租"),
    // 合租
    SINGLE(1,"合租");
    int code;
    String des;

    RentWayEnum(int code, String des) {
        this.code = code;
        this.des = des;
    }
    public static RentWayEnum getFromDes(String des){
        for (RentWayEnum rentWayEnum : RentWayEnum.values()){
            if (rentWayEnum.des.equals(des)){
                return rentWayEnum;
            }
        }
        return null;
    }

    public static RentWayEnum getFromCode(int code){
        for (RentWayEnum rentWayEnum : RentWayEnum.values()){
            if (rentWayEnum.code == code){
                return rentWayEnum;
            }
        }
        return null;
    }

    public int getCode() {
        return code;
    }

    public String getDes() {
        return des;
    }
}
