from sqlalchemy.orm import sessionmaker
from myveido.models import (db_dyy, Category, VideoType, Star, Director,
                             VideoDetails, VideoContent)

# 连接数据库，返回对象
def linkDb(dataBase):
    db = dataBase
    Session = sessionmaker(bind=db)
    session = Session()

    return session


# 查询片面是否重复
def getTitleRepeat(title_name):
    print(title_name)
    dyy = linkDb(db_dyy())
    query_details_id = dyy.query(VideoDetails).filter(VideoDetails.title==title_name).first()

    details_id = ''
    if query_details_id:
        details_id = query_details_id.id
    else:
        details_id = None
    return details_id


# 保存导演
def getDirectorId(director):
    dyy = linkDb(db_dyy())
    query_director = dyy.query(Director).filter(Director.name==director).first()

    director_id = ''
    if query_director:
        director_id = query_director.id
    else:
        director = Director(name=director)
        dyy.add(director)
        dyy.commit()

        director_id = director.id

    return director_id

# 保存影视类型
def getVideoTypeId(videotype):
    query_list = []
    if videotype == []:
        return query_list
    for index in range((len(videotype))):
        videotypes = videotype[index]
        dyy = linkDb(db_dyy())
        query_videotype = dyy.query(VideoType).filter(VideoType.name == videotypes).first()

        videotype_id = ''
        if query_videotype:
            videotype_id = query_videotype.id
        else:
            new_type = VideoType(name=videotypes)
            dyy.add(new_type)
            dyy.commit()

            videotype_id = new_type.id

        query_list.append(videotype_id)

    return query_list

# 保存明星
def getStarId(star):
    query_list = []
    if star == []:
        return query_list
    for index in range((len(star))):
        stars = star[index]
        dyy = linkDb(db_dyy())
        query_star = dyy.query(Star).filter(Star.name == stars).first()

        star_id = ''
        if query_star:
            star_id = query_star.id
        else:
            new_star = Star(name=stars)
            dyy.add(new_star)
            dyy.commit()

            star_id = new_star.id

        query_list.append(star_id)

    return query_list

# 字段去空格换行
def FieldClean(strFiled):
    field = strFiled.replace(' ', '')
    field = field.replace('\n', '')
    field = field.replace('\t', '')

    return field