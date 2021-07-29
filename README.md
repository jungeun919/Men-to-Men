# Matching Mentor To Mentee

**파일 구조**

* 프로젝트 폴더명: mentomen

* 앱 폴더:

    * recruit (멘토 멘티 모집)
    * accounts (회원가입, 로그인/로그아웃)
    * mail (상대방에게 메일 전송)

<br>

**url 구조**

|app|url|설명|
|---|---|---|
|accounts|domain/accounts/login|로그인|
||domain/accounts/logout|로그아웃|
||domain/accounts/signup|회원가입|
|mail|domain/mail|이메일 작성 폼|
||domain/mail/send|이메일 전송|
|recruit|domain/|메인 페이지|
||domain/post|전체 글 띄우기|
||domain/post/번호|상세 페이지 띄우기|
||domain/post/new_post|새 글 작성하기|
||domain/post/번호/remove|글 삭제하기|
||domain/comment_new/번호|댓글 폼|
||domain/update/comment_new/번호|댓글 수정하기|
||domain/delete/comment_new/번호|댓글 삭제하기|