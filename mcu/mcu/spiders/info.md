# TOMATO
movie links = response.css('div.article_movie_title h2 a::attr(href)').getall()
synopsis = response.css('div#movieSynopsis::text').get()
production_team = response.css('div.meta-label.subtle +div a::text').getall()[:-1]
release_date_theatres = response.css('div.meta-label.subtle +div time::text').getall()[0]
release_date_streaming = response.css('div.meta-label.subtle +div time::text').getall()[1]
runtime = response.css('div.meta-label.subtle +div time::text').getall()[-1]
box_office = response.css('div.meta-label.subtle +div::text').getall()[-8]
distributor = response.css('div.meta-label.subtle +div::text').getall()[-5]
cast_crew = response.css('div.cast-item.media.inlineBlock div.media-body a span::text').getall()

# TOMATO_REVIEWS
reviews = response.css('div.the_review::text').getall()