package com.rta.web.web;

import com.rta.web.dom.House;
import com.rta.web.mapper.HouseMapper;
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

    @RequestMapping("/greeting")
    public String greeting(@RequestParam(value="name", required=false, defaultValue="World") String name, Model model) {
        model.addAttribute("name", name);
        return "greeting";
    }

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
    List<House> getHouseBySubway(@RequestParam("subway") Integer subway){
        return mapper.selectHouseBySubway(subway);
    }

    @RequestMapping(value = "/queryBySource")
    public @ResponseBody List<House> getHouseBySource(@RequestParam("source") String source){
        return mapper.selectHouseBySource(source);
    }

    @RequestMapping(value = "/queryByVillage")
    public @ResponseBody List<House> getHouseByVillage(@RequestParam("village") String village){
        return mapper.selectHouseByVillage(village);
    }
    @RequestMapping(value = "/queryAll")
    public @ResponseBody List<House> getHouse(@RequestParam("source") String source, @RequestParam("subway") Integer subway){
        return mapper.selectHouseByAll(source,subway);
    }

}
