package com.rta.web.web;

import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
@EnableAutoConfiguration
public class IndexController {

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
    public String[] getCity(){
        String[] strings = new String[2];
        strings[0] = "北京";
        strings[1] = "西安";
        return strings;
    }
}
