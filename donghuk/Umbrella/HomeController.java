package com.spring.controller;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.text.DateFormat;
import java.util.Date;
import java.util.Locale;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

/**
 * Handles requests for the application home page.
 */
@Controller
public class HomeController {
	
	private static final Logger logger = LoggerFactory.getLogger(HomeController.class);
	
	/**
	 * Simply selects the home view to render by returning its name.
	 */
	@RequestMapping(value = "/", method = RequestMethod.GET)
	public String home() {
		
		
		return "index";
	}
	@GetMapping("umbrella")
	public String umb1() {
		return "umbrella2";
	}
	
	
	
	
	@PostMapping("/umbrella/save_center")
	public void umbrella_save_center(String center_lat, String center_lng) {
		
		File file = new File("d:\\center.txt");
		FileWriter writer = null;
		
		try {
			writer = new FileWriter(file);
			writer.write(center_lat+" "+center_lng);
			writer.flush();
			
			System.out.println("done");
		} catch (Exception e) {
			e.printStackTrace();
		}finally {
			try {
				if(writer != null) {
					writer.close();
				}
			} catch (Exception e2) {
				e2.printStackTrace();
			}
		}
		
	}
	
	@PostMapping("/umbrella/get_center")
	@ResponseBody
	public String umbrella_get_center() {
		String latlng = "";
		File file = new File("d:\\center.txt");
		try(FileReader filereader = new FileReader(file);
			BufferedReader br = new BufferedReader(filereader)
			) {
			latlng = br.readLine();
			System.out.println(latlng);
			
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			
		}
		System.out.println("get_center : "+latlng);
		return latlng;
	}

	
	@PostMapping("/umbrella/save_level")
	public void umbrella_save_level(String level) {
		
		File file = new File("d:\\level.txt");
		FileWriter writer = null;
		
		try {
			writer = new FileWriter(file, false);
			writer.write(level);
			writer.flush();
			
			System.out.println("done");
		} catch (Exception e) {
			e.printStackTrace();
		}finally {
			try {
				if(writer != null) {
					writer.close();
				}
			} catch (Exception e2) {
				e2.printStackTrace();
			}
		}
		
	}
	
	@PostMapping("/umbrella/get_level")
	@ResponseBody
	public String umbrella_get_level() {
		String level = "";
		File file = new File("d:\\level.txt");
		try(FileReader filereader = new FileReader(file);
			BufferedReader br = new BufferedReader(filereader)
			) {
			level = br.readLine();
			System.out.println("get_level1 : "+level);
			
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			
		}
		System.out.println("get_level2 : "+level);
		return level;
	}
}
