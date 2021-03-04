from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker
from itemadapter import ItemAdapter
from myveido.models import (db_dyy, Category, VideoType, Star, Director,
                             VideoDetails, VideoContent, VideodetailsVideotype, VideodetailsStar)
from myveido.utils import (getTitleRepeat, getDirectorId, FieldClean, getStarId, getVideoTypeId)

@contextmanager
def session_scope(Session):
	"""Provide a transactional scope around a series of operations."""
	session = Session()
	session.expire_on_commit = False
	try:
		yield session
		session.commit()
	except:
		session.rollback()
		raise
	finally:
		session.close()


class MyveidoPipeline:
	def __init__(self):
		engine = db_dyy()
		self.Session = sessionmaker(bind=engine)

	def open_spider(self, spider):
		pass

	def process_item(self, item, spider):
		detail_id = getTitleRepeat(item['title'][0])
		if not detail_id:
			director_id = getDirectorId(item['director'][0])
			videodetails = VideoDetails(
				title = item['title'][0],
				score = item['score'][0],
				introduction = FieldClean(item['introduction'][0]),
				thumb = item['thumb'][0],
				director_id = director_id,
				category_id = 1,
				status = 0,
				is_new = 0,
				)
			with session_scope(self.Session) as session:
				session.add(videodetails)
				session.commit()

			star_ids = getStarId(item['star'])
			if star_ids:
				for index in range(len(star_ids)):
					videodetailsstar = VideodetailsStar(
						videodetails_id = videodetails.id,
						star_id = star_ids[index],
						)
					with session_scope(self.Session) as session:
						session.add(videodetailsstar)
						session.commit()

			videotype_ids = getVideoTypeId(item['videotype'])
			if videotype_ids:
				for index in range(len(videotype_ids)):
					videotype = VideodetailsVideotype(
						videodetails_id = videodetails.id,
						videotype_id = videotype_ids[index],
						)
					with session_scope(self.Session) as session:
						session.add(videotype)
						session.commit()

		else:
			print('重复了')

	def close_spider(self, spider):
		pass
