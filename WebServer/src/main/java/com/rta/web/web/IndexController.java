package com.rta.web.web;

import com.rta.web.dom.HouseV2;
import com.rta.web.mapper.CityMapper;
import com.rta.web.mapper.HouseMapper;
import com.rta.web.service.ConvertService;
import com.rta.web.utils.enums.CityNameEnum;
import com.rta.web.utils.enums.RentWayEnum;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.LinkedList;
import java.util.List;

@Controller
@EnableAutoConfiguration
public class IndexController {

    @Autowired
    HouseMapper houseMapper;
    @Autowired
    CityMapper cityMapper;
    @Autowired
    ConvertService convertService;

    @RequestMapping("/")
    public String index(){
        return "index";
    }

    @RequestMapping("/getCity")
    public @ResponseBody List<String> getCity(){
        LinkedList<String> list = new LinkedList<>();
        list.add("北京");
        list.add("西安");
        return list;
    }

    @RequestMapping(value = "/queryBySubway")
    public @ResponseBody
    List<HouseV2> getHouseBySubway(@RequestParam("subway") Integer subway){
        return convertService.convertList(houseMapper.selectHouseBySubway(subway));
    }

    @RequestMapping(value = "/queryBySource")
    public @ResponseBody List<HouseV2> getHouseBySource(@RequestParam("source") String source){
        return convertService.convertList(houseMapper.selectHouseBySource(source));

    }

    @RequestMapping(value = "/queryByVillage")
    public @ResponseBody List<HouseV2> getHouseByVillage(@RequestParam("village") String village){
        return convertService.convertList(houseMapper.selectHouseByVillage(village));
    }
    @RequestMapping(value = "/queryAll")
    public @ResponseBody List<HouseV2> getHouse(@RequestParam("source") String source, @RequestParam("subway") Integer subway){
        return convertService.convertList(houseMapper.selectHouseByAll(source,subway));
    }
    @RequestMapping(value = "/queryByRentWay")
    public @ResponseBody List<HouseV2> getHouseByRentWay(@RequestParam("rentWay") String rentWay){
        String des;
        String all = "all";
        if (all.equals(rentWay)){
            des = "整租";
        }else {
            des = "合租";
        }
        RentWayEnum rentWayEnum = RentWayEnum.getFromDes(des);
        if (rentWayEnum == null){
            return null;
        }
        return convertService.convertList(houseMapper.selectHouseByRentWay(rentWayEnum.getCode()));
    }
    @RequestMapping(value = "/queryByCity")
    public @ResponseBody List<HouseV2> getHouseByCity(@RequestParam("city") String city){
        CityNameEnum nameEnum = CityNameEnum.getByAbbr(city);
        Integer code = cityMapper.selectCityCodeByName(nameEnum.getName());
        return convertService.convertList(houseMapper.selectHouseByCityCode(code));
    }

    @RequestMapping(value = "/queryByPriceLoAndHi")
    public @ResponseBody List<HouseV2> getHouseByPrice(@RequestParam("lo") Integer lo, @RequestParam("hi") Integer hi){
        return convertService.convertList(houseMapper.selectHouseByPriceLoAndHi(hi,lo));
    }

    @RequestMapping(value = "/queryByPriceBigThanHi")
    public @ResponseBody List<HouseV2> getHouseByPrice( @RequestParam("hi") Integer hi){
        return convertService.convertList(houseMapper.selectHouseByPriceBigThanHi(hi));
    }
}
