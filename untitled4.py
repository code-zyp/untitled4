from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

#用户表
# create table users(
#     id int primary key autoincrement,
#     username varchar(100) not null
#
# )
#文章表
# create table article(
#     id int primary key autoincrement,
#     title varchar(100) not null,
#     content text not null
#     author_id int,
#     foregin key 'author_id references 'users.id'
# )


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(100),nullable=False)

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text,nullable=False)
    author_id = db.Column(db.Integer,db.ForeignKey('user.id'))#这里用表名不用模型名
    author = db.relationship('User',backref=db.backref('articles'))#backref为反向引用。通过自己定义的articles可以访问到这个作者所有的文章



db.create_all()
@app.route('/')
def index():
    #要想添加一篇文章，因为要添加文章首先要有用户，所以应该先建立用户
    user1 =User(username='zyp123')
    # db.session.add(user1)
    # db.session.commit()
    # article =Article(title='aaa',content='bbb',author_id=1)
    # db.session.add(article)
    # db.session.commit()
    # author = User.query.filter(User.username=='zyp123').first()
    # author.articles


    # article = Article(title='aaa',content='bbb')
    # article.author=User.query.filter(User.id==1).first()
    # db.session.add(article)
    # db.session.commit()

    # article =Article.query.filter(Article.title=='aaa').first()
    # print('sername:%s'%article.author.username)

    # article =Article(title='133',content='222')
    # article.author=User.query.filter(User.username=='zyp123').first()
    # db.session.add(article)
    # db.session.commit()

    # user = User.query.filter(User.username == 'zyp123').first()
    # result = user.articles
    # for article in result:
    #     print('-'*10)
    #     print(article.title,article.content)
    #
    # return 'Hello World!'


if __name__ == '__main__':
    app.run()


#author =db.relationship('User',backref=db.backref('articles'))
#解释：给Article这个模型添加一个author母性，可以访问这篇文章的作者的数据像访问普通模型一样
#backref是定义反向引用，可以通过User这个模型访问这个模型所写的所有文章