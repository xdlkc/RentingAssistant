package com.rta.web.mapper;

import com.rta.web.dom.House;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

/**
 * @author lkc
 * @Date 17-12-17 下午4:02
 */
@Mapper
public interface HouseMapper {
    /**
     * 获取房屋信息
     * @param id
     * @return House
     */
    House selectHouseById(@Param("id") Long id);

    /**
     * 根据地铁线筛选房屋
     * @param subway
     * @return
     */
    House selectHouseBySubway(@Param("subway") Integer subway);

    /**
     * 根据城市代码筛选房屋
     * @param cityCode
     * @return
     */
    House selectHouseByCityCode(@Param("cityCode") Integer cityCode);

    /**
     * 根据小区筛选房屋信息
     * @param village
     * @return
     */
    House selectHouseByVillage(@Param("village") String village);
}
