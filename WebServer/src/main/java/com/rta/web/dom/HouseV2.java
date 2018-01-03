package com.rta.web.dom;

import lombok.Data;

/**
 * @author lkc
 * @date 18-1-3 下午2:32
 */
@Data
public class HouseV2 {
    long id;
    // 房屋标题
    String title;
    // 房屋链接
    String houseLink;
    // 链接的md5加密结果
    String hashLink;
    // 房屋面积
    int meters;
    // 卧室个数
    int bedroom;
    // 客厅个数
    int livingRoom;
    // 卫生间个数
    int toilet;
    // 浏览人数
    int peopleSum;
    // 房屋来源
    String source;
    // 租赁方式
    String rentWay;
    // 城市代码
    String city;
    // 所在大区
    String regionLo;
    // 所在小区
    String regionHi;
    // 附近地铁
    int subway;
    // 价格
    int price;
    // 其他信息
    String detail;
    // 小区
    String village;
}
