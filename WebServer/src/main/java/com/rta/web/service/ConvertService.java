package com.rta.web.service;

import com.rta.web.dom.House;
import com.rta.web.dom.HouseV2;
import com.rta.web.mapper.CityMapper;
import com.rta.web.utils.enums.RentWayEnum;
import org.springframework.beans.BeanUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.LinkedList;
import java.util.List;
import java.util.Objects;

/**
 * @author lkc
 * @date 18-1-3 下午2:34
 */
@Service
public class ConvertService {
    @Autowired
    CityMapper cityMapper;

    public HouseV2 convert(House house){
        HouseV2 houseV2 = new HouseV2();
        BeanUtils.copyProperties(house,houseV2);
        houseV2.setCity(cityMapper.selectCityNameByCode(house.getCityCode()));
        houseV2.setRentWay(Objects.requireNonNull(RentWayEnum.getFromCode(house.getRentWay())).getDes());
        return houseV2;
    }
    public List<HouseV2> convertList(List<House> houses){
        LinkedList<HouseV2> houseV2s = new LinkedList<>();
        for (House house : houses){
            houseV2s.add(convert(house));
        }
        return houseV2s;
    }
}
