_尚未完成的项目_

*This project is unfinished*  

计划：做成在线定位系统，与https://github.com/JohnDing1995/WebApp 合并

*I'm planning to combine with another project of mine, a web app based in flask*

## Requirement 

Python 3.6

Scrapy 

Pymongo

## Usage

1. Clone this repository 

2. cd to the root of the project, run `scrapy crawl ad_information`

3. The data will shown in your mongdb database,like this![屏幕快照 2017-03-13 下午10.49.52](http://p1.bqimg.com/4851/6e725b0c04c107f5.png)

4. Yan can query the database as according to your own need

    eg. To find the admissions of CS master@north Carolina state university(NCSU),you can query like this

   ![屏幕快照 2017-03-14 上午9.08.03 1](http://p1.bqimg.com/4851/86b362a890bf11be.png)


## Update log

* 2017/3/11 add mongdb data storage,
  * bug to fix:some void data didn't added to db, which makes fields don't match with each other
* 2017/3/13 Rewrite Selector modual  with regular expression , now the void data will be stored in the database, and the bug fixed;Optimize the database storage, now each admission information can be stored as a single object

