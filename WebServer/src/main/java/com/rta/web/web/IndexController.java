package com.rta.web.web;

import com.rta.web.dom.House;
import com.rta.web.dom.HouseV2;
import com.rta.web.mapper.HouseMapper;
import com.rta.web.service.ConvertService;
import com.rta.web.utils.enums.RentWayEnum;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.LinkedList;
import java.util.List;

@Controller
@EnableAutoConfiguration
public class IndexController {

    @Autowired
    HouseMapper mapper;
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
        return convertService.convertList(mapper.selectHouseBySubway(subway));
    }

    @RequestMapping(value = "/queryBySource")
    public @ResponseBody List<HouseV2> getHouseBySource(@RequestParam("source") String source){
        return convertService.convertList(mapper.selectHouseBySource(source));

    }

    @RequestMapping(value = "/queryByVillage")
    public @ResponseBody List<HouseV2> getHouseByVillage(@RequestParam("village") String village){
        return convertService.convertList(mapper.selectHouseByVillage(village));
    }
    @RequestMapping(value = "/queryAll")
    public @ResponseBody List<HouseV2> getHouse(@RequestParam("source") String source, @RequestParam("subway") Integer subway){
        return convertService.convertList(mapper.selectHouseByAll(source,subway));
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
        return convertService.convertList(mapper.selectHouseByRentWay(rentWayEnum.getCode()));
    }


}
