import course
import song

COURSES = [
    course.Course(period=1,
                  name='Intro to Computer Science',
                  teacher_name='Ms. Lee',
                  resource_name='repl.it',
                  resource_url='https://repl.it/'),
    course.Course(period=2,
                  name='Alg 2 Honors',
                  teacher_name='Mr. Shelton',
                  resource_name='Khan Academy',
                  resource_url='https://www.khanacademy.org/'),
    course.Course(period=3,
                  name='AP Lang. and Comp.',
                  teacher_name='Ms. McCann',
                  resource_name='Google Docs',
                  resource_url='https://docs.google.com/'),
    course.Course(period=4,
                  name='Spanish 3',
                  teacher_name='Ms. Geiser',
                  resource_name='Wikipedia: Spain',
                  resource_url='https://en.wikipedia.org/wiki/Spain'),
    course.Course(period=5,
                  name='US History',
                  teacher_name='Ms. Clements',
                  resource_name='History Day: ERA',
                  resource_url='http://95223748.nhd.weebly.com/'),
    course.Course(period=6,
                  name='Biotechnology 1/2',
                  teacher_name='Mr. Ng',
                  resource_name='NCBI',
                  resource_url='https://www.ncbi.nlm.nih.gov/')
]


TOP_TEN_SONGS = [
    song.Song(title="Counting Stars",
                artist_name='OneRepublic',
                youtube_url='https://www.youtube.com/watch?v=hT_nvWreIhg'),
    song.Song(title="Ignorance",
                artist_name='Paramore',
                youtube_url='https://www.youtube.com/watch?v=OH9A6tn_P6g'),
    song.Song(title="The Kids Aren't Alright",
                artist_name='Fall Out Boy',
                youtube_url='https://www.youtube.com/watch?v=WR7U7_cKJw4'),
    song.Song(title="The Good, the Bad, and the Dirty",
                artist_name='Panic! At the Disco',
                youtube_url='https://www.youtube.com/watch?v=Nu55xS1TdoU'),
    song.Song(title="Waiting For the End",
                artist_name='Linkin Park',
                youtube_url='https://www.youtube.com/watch?v=5qF_qbaWt3Q'),
    song.Song(title="Too Soon",
                artist_name='Hey Ocean!',
                youtube_url='https://www.youtube.com/watch?v=_nhssMi2FtA'),
    song.Song(title="Disenchanted",
                artist_name='My Chemical Romance',
                youtube_url='https://www.youtube.com/watch?v=j_MlBCb9-m8'),
    song.Song(title="Let's Hurt Tonight",
                artist_name='OneRepublic',
                youtube_url='https://www.youtube.com/watch?v=8wGN7D03Nho'),
    song.Song(title="Pool",
                artist_name='Paramore',
                youtube_url='https://www.youtube.com/watch?v=3m8ElO9Y50Y'),
    song.Song(title="Sunshine Riptide",
                artist_name='Fall Out Boy',
                youtube_url='https://www.youtube.com/watch?v=Vgj5-vwkFwQ')
]

