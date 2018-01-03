package com.rta.web.mapper;

import com.rta.web.dom.House;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;

import java.util.LinkedList;

/**
 * @author lkc
 * @Date 17-12-17 下午4:02
 */
@Mapper
public interface HouseMapper {
    /**
     * 根据地铁线筛选房屋
     * @param subway
     * @return
     */
    @Select("select * from house where subway = #{subway};")
    LinkedList<House> selectHouseBySubway(int subway);


    /**
     * 根据来源筛选
     * @param source
     * @return
     */
    @Select("select * from house where source = #{source};")
    LinkedList<House> selectHouseBySource(@Param("source") String  source);

    /**
     * 根据小区筛选房屋信息
     * @param village
     * @return
     */
    @Select("select * from house where village = #{village};")
    LinkedList<House> selectHouseByVillage(@Param("village") String village);

    /**
     * 根据所有必要信息筛选
     * @param source
     * @param subway
     * @return
     */
    @Select("select * from house where source = #{source} and subway = #{subway}; ")
    LinkedList<House> selectHouseByAll(@Param("source") String source, @Param("subway") Integer subway);

    /**
     * 根据租赁方式筛选
     * @param rentWay
     * @return
     */
    @Select("select * from house where rent_way = #{rentWay};")
    LinkedList<House> selectHouseByRentWay(@Param("rentWay") Integer rentWay );
}
