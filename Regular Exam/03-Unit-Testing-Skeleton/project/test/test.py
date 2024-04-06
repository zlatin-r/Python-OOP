from unittest import TestCase, main
from project.social_media import SocialMedia


class TestSocialMedia(TestCase):
    def setUp(self):
        self.social_media = SocialMedia("TestName", "YouTube", 50, "Fun")

    def test_init(self):
        self.assertEqual(self.social_media._username, "TestName")
        self.assertEqual(self.social_media._platform, "YouTube")
        self.assertEqual(self.social_media._followers, 50)
        self.assertEqual(self.social_media._content_type, "Fun")
        self.assertEqual(self.social_media._posts, [])

    def test_validate_and_set_platform_invalid_value(self):
        with self.assertRaises(ValueError) as ve:
            self.social_media.platform = "facebook"

        self.assertEqual("Platform should be one of ['Instagram', 'YouTube', 'Twitter']", str(ve.exception))

    def test_validate_and_set_platform_valid_value(self):
        self.assertEqual(self.social_media.platform, "YouTube")

        self.social_media.platform = "Instagram"
        self.assertEqual(self.social_media.platform, "Instagram")

    def test_create_post(self):
        res = self.social_media.create_post("test_post")
        expect = [{'comments': [], 'content': 'test_post', 'likes': 0}]

        self.assertEqual(res, "New Fun post created by TestName on YouTube.")
        self.assertEqual(self.social_media._posts, expect)
        self.assertEqual(len(self.social_media._posts), 1)

    def test_create_post_second_happy_case(self):
        post_content = "Test post"
        self.assertEqual(self.social_media.create_post(post_content),
                         f"New {self.social_media._content_type} "
                         f"post created by {self.social_media._username} "
                         f"on {self.social_media._platform}.")

    def test_followers_happy_case(self):
        self.assertEqual(self.social_media._followers, 50)

    def test_followers_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.social_media.followers = -5

        self.assertEqual("Followers cannot be negative.", str(ve.exception))

    def test_like_post_index_one(self):
        self.social_media.create_post("test")
        self.social_media.create_post("test_post")
        res = self.social_media.like_post(1)

        self.assertEqual("Post liked by TestName.", res)

    def test_like_post_index_over_max(self):
        self.social_media.create_post("test")
        self.social_media.create_post("test_post")

        res = self.social_media.like_post(1)
        res = self.social_media.like_post(1)
        res = self.social_media.like_post(1)
        res = self.social_media.like_post(1)
        res = self.social_media.like_post(1)
        res = self.social_media.like_post(1)
        res = self.social_media.like_post(1)
        res = self.social_media.like_post(1)
        res = self.social_media.like_post(1)
        res = self.social_media.like_post(1)
        res = self.social_media.like_post(1)

        self.assertEqual("Post has reached the maximum number of likes.", res)
        self.assertEqual(len(self.social_media._posts), 2)

    def test_like_post_index_max(self):
        for i in range(10):
            self.social_media.create_post("test")
            self.assertEqual(self.social_media.like_post(0), "Post liked by TestName.")
        self.assertEqual(self.social_media.like_post(0), "Post has reached the maximum number of likes.")

    def test_like_post_invalid_index(self):
        self.social_media.create_post("test")

        self.social_media.create_post("test_post")
        res = self.social_media.like_post(-1)

        self.assertEqual("Invalid post index.", res)

    def test_like_post_invalid_index_over_ten(self):
        self.social_media.create_post("test")

        self.social_media.create_post("test_post")
        res = self.social_media.like_post(11)

        self.assertEqual("Invalid post index.", res)

    def test_comment_on_post_valid_len(self):
        self.social_media.create_post("test")
        self.social_media.create_post("test_post")

        res = self.social_media.comment_on_post(1, "xaxaxaxaxaa")

        self.assertEqual("Comment added by TestName on the post.", res)
        self.assertEqual(len(self.social_media._posts), 2)

    def test_comment_on_post_invalid_len(self):
        self.social_media.create_post("test")
        self.social_media.create_post("test_post")

        res = self.social_media.comment_on_post(1, "xaxaxaxax")

        self.assertEqual("Comment should be more than 10 characters.", res)
        self.assertEqual(len(self.social_media._posts), 2)


if __name__ == '__main__':
    main()
