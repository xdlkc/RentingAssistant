package com.rta.web.mapper;

import com.rta.web.dom.City;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;

import java.util.LinkedList;

/**
 * @author lkc
 * @date 18-1-3 下午2:35
 */
@Mapper
public interface CityMapper {
    /**
     *
     * @param cityCode
     * @return
     */
    @Select("select city_name from city where city_code = #{cityCode}")
    String selectCityNameByCode(int cityCode);

    @Select("select city_code from city where city_name = #{cityName}")
    Integer selectCityCodeByName(String cityName);
}
