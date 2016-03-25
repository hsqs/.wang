title: Mybatis 使用技巧总结
date: 2015-12-27

这是[中文官方文档](http://mybatis.org/mybatis-3/zh/)，前后一共用了大概1年时间，当时为了赶进度，只学了些基本的用法，后来随着业务的复杂，SQL查询也越来越复杂，就积累了一些Mybatis的使用知识。Mybatis的基本用法和优点什么的就不用多介绍了，下面直接开撸吧。
1、在使用 foreach 标签时，通常用于构建 IN 子查询或插入数据语句，构建 IN 语句的语法如下：
<foreach collection="list" index="index" item="m" open="(" separator="," close=")">
    #{m}
</foreach>
foreach 的各项参数就不用多解释了，这里，open 和 close 都显示的写到了foreach标签里。同理，当构建插入多条数据的语句时，同样的语法，不过稍有点变化：
<foreach collection="list" index="index" item="m" separator=",">
    (#{m.id}, #{m.name})
</foreach>
注意，foreach 里的语句是带了圆括号，去掉了open 和 close 属性，分隔符依旧是,，这是其中一种对values后面SQL的一种分解方式，或者用下面这种：
<foreach collection="list" index="index" item="m" open="(" separator="),(" close=")">
    #{m.id}, #{m.name}
</foreach>
这里唯一注意的是 separator 的变化，这两种插入数据时的写法，效果都是一致的。想到这里，separator 可以是多个字符，那可不可以是 AND、OR 这样的分隔符呢？答案是肯定的，如此一来，foreach 可以构造多个重复条件的方法就灵活的多了。

2、在传入多个参数到Mybatis的时候，如果是构建像上面的 IN 语句或插入多条数据，可以用 List 来达到目的。如果是多个不同类型的参数，有的是 String，有的是List 的话，一般会用 Map<String, Object>，把Key作为参数名称，真正的参数放到Value中，在mapper文件里通过#{Key}的方式可以取到参数。这种方法虽然是极好的，但每次都要构造一个Map，然后把参数再一个个put进去，确实麻烦。这里就可以使用注解，省去这一堆步骤。
public List<String> selectName(@Param("address")List<Integer> addrs, @Param("gender")char gds);
调用的时候，只需要把相应的参数传进去即可，在mapper文件里，用 @Param 里的注解名称来取参数，例如这里的address和gender，和Map的取用方式一样，#{address} 就可以拿到参数了。

3、在mapper文件里写SQL时，每个SQL的id都要对应一个DAO中的接口名称，保证他们可以找到彼此，其实，对于比较简单的一两行的SQL，可以不用在mapper文件里写配置，直接在Java代码里添加注解的方式来实现。
@Select("SELECT name FROM user WHERE province_id = #{address} AND gender = #{gender}")
public List<String> selectName(@Param("address")Integer address, @Param("gender")char gender);
除了@Select 注解，还有@Insert、@Update、@Delete，使用方法同上。这样SQL和Java代码放在一起，
查看起来非常的方便。这四个注解还有其他属性，不过我也没用过，就不作介绍了。