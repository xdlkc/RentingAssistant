package com.rta.web.dom;

import lombok.Data;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

/**
 * @author lkc
 * @date 17-12-29 上午12:00
 */
@Entity
@Data
public class City {
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Id
    long id;
    String cityName;
    String provinceName;
    int cityCode;
}
