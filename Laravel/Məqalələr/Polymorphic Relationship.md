# Polymorphic Relationship in Laravel
Düşünək ki, bizim blogs və news cədvəllərimiz var.

> Blogs
-id
-name
News
-id
-name

Bunların hər birininin tagləri olsa, onda biz əlavə 2 cədvəl yaramalı olacayıq. “blog_tags” və “news_tags”. Sonra isə ‘hasMany’ sayəsində blog və ya xəbərlərimizə aid tagləri götürə bilərik.

> Blog_tag
-id
-blog_id
-tag
News_tags
-id
-news_id
-tag

Ancaq biz polymorphic relationship işlətsək 2 və daha çox cədvəl üçün yalnız 1 ədəd cədvəl yaradaraq taglərimizi onun içərisində saxlıya bilərik.
Gəlin buna aid nümunəyə baxaq.
Tag model və migrations yaradırıq.

`php artisan make:model Tag -m`

Tags migrationsa daxil oluruq:

> Schema::create(‘tags’, function (Blueprint $table) {
    $table->id();
    $table->string(‘name’);
    $table->unsignedBigInteger(‘taggable_id’);
    $table->string(‘taggable_type);
    $table->timestamps();
});

taggable_id - bizim news və ya blogs cədvəlində id təmsil edir.
taggable_type - isə modelimiz olacaq. Məsələn App\Models\News və ya App\Models\Blog.
name - isə tagimizin adıdır.
Table yaranması üçün migrate edək.

`php artisan migrate`

Daxil oluruq News və Blog Modelimizə. Burada tags metodu yaradırıq:

> use HasFactory;
protected $guarded = [];
public function tags()
{
    return $this->morphMany(Tag::class,’taggable’);
}

Daxil oluruq Tag modelimizə və bunun əksini qeyd edirik:

> class Tag extends Model
{
    use HasFactory;
    protected $guarded = [];
    public function taggable()
    {
        return $this->morphTo();
    }
}

Gəlin tinker işlədərək saxta taglər əlavə edək. Terminalı açaq və kodları ardıcıllıqla icra edək:

`php artisan tinker`

`$blog = Blog::find(1);`

`$blog->tags()->create([‘name’=>’macəra’]);php artisan tinker`

Nəticəyə göz ataq:

> => App\Models\Tag {#4134
    name: “macəra”,
    taggable_id: 1,
    taggable_type: “App\Models\Blog”,
    updated_at: “2021–07–28 12:16:13”,
    created_at: “2021–07–28 12:16:13”,
    id: 1,
}

Nəticə: IDsi 1 olan blogun tagi “macəra”dır.
Gəlin indi də news cədvəlimizə saxta tag əlavə edək.

`php artisan tinker`

`$news = News::find(1);`

`$news->tags()->create([‘name’=>’qorxu’]);`

Nəticə:

> App\Models\Tag {#4386
    name: “qorxu”,
    taggable_id: 1,
    taggable_type: “App\Models\News”,
    updated_at: “2021–07–28 12:37:21”,
    created_at: “2021–07–28 12:37:21”,
    id: 2,
}

Nəticə: IDsi 1 olan xəbərin tagi “qorxu”dur.
İndi isə blogumuz ilə birlikdə ona aid taglari necə götürə bilərik ona baxaq:
Daxil olaq web.php

> Route::get(‘/blog’, function () {
    $blog = Blog::with(‘tags’)->find(1);
    return $blog;
});

Siz bunu controllerdə də yaza bilərsiz. Bizə qaytarılan nəticə:

![1_nF-CqUqF0VSY7sNWQOG8lQ](https://user-images.githubusercontent.com/78316758/149944878-cb092a5b-3950-4ce6-9554-353bc0352b6b.png)

