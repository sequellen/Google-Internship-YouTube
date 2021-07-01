"""A video player class."""

from .video_library import VideoLibrary
import random


def get_all_videos(self):
    pass


class VideoPlayer:
    """A class used to represent a Video Player."""
    currently_playing = None
    video_paused = False
    playlists = {}
    videodict = {}

    def __init__(self):
        self._video_library = VideoLibrary()
        self.currently_playing = None
        self.video_paused = False
        self.playlists = {}
        for video in self._video_library.get_all_videos():
            self.videodict[video.video_id] = video

    def number_of_videos(self):
        num_videos = len(self.videodict.keys())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        all_videos = {}
        for vid in self.videodict.keys():
            all_videos[self.videodict[vid].title] = self.videodict[vid]
        sortednames = sorted(all_videos.keys(), key=lambda x: x.lower())
        print("Here's a list of all available videos:")
        for vid in sortednames:
            if not all_videos[vid].flagged:
                print(all_videos[vid].title + ' (' + all_videos[vid].video_id + ') [' + (
                    ' '.join([tag for tag in all_videos[vid].tags if isinstance(tag, str)])) + ']')
            else:
                print(all_videos[vid].title + ' (' + all_videos[vid].video_id + ') [' + (
                    ' '.join([tag for tag in all_videos[vid].tags if isinstance(tag, str)])) + '] - FLAGGED (reason: ' +
                      all_videos[vid].flagreason + ")")

    def play_video(self, video_id):
        """Plays the respective video.
        Args:
            video_id: The video_id to be played.
        """
        video = self._video_library.get_video(video_id)
        if video and not video.flagged:
            if not self.currently_playing:
                self.currently_playing = video
                print('Playing video: ' + self.currently_playing.title)
                self.video_paused = False
            else:
                print('Stopping video: ' + self.currently_playing.title)
                self.currently_playing = video
                print('Playing video: ' + self.currently_playing.title)
                self.video_paused = False
        elif video and video.flagged:
            print("Cannot play video: Video is currently flagged (reason: " + video.flagreason + ")")
        else:
            print("Cannot play video: Video does not exist")

    def stop_video(self):
        """Stops the current video."""
        if not self.currently_playing:
            print("Cannot stop video: No video is currently playing")
        else:
            print('Stopping video: ' + self.currently_playing.title)
            self.currently_playing = None
            self.video_paused = False

    def play_random_video(self):
        """Plays a random video from the video library."""
        all_videos = [key for key in self.videodict.keys()]
        if all_videos:
            vid = random.choice(all_videos)
            if not self.videodict[vid].flagged:
                self.play_video(self.videodict[vid].video_id)
            else:
                count = 0
                while (self.videodict[vid].flagged and count < len(list(all_videos))):
                    vid = random.choice(all_videos)
                    count += 1
                if not self.videodict[vid].flagged:
                    self.play_video(self.videodict[vid].video_id)
                else:
                    print("No videos available")

        else:
            print("No videos available")

    def pause_video(self):
        """Pauses the current video."""
        if self.currently_playing and not self.video_paused:
            self.video_paused = True
            print("Pausing video: " + self.currently_playing.title)
        elif not self.currently_playing:
            self.video_paused = False
            print("Cannot pause video: No video is currently playing")
        else:
            print("Video already paused: " + self.currently_playing.title)

    def continue_video(self):
        """Resumes playing the current video."""
        if self.currently_playing and self.video_paused:
            self.video_paused = False
            print("Continuing video: " + self.currently_playing.title)
        elif not self.currently_playing:
            self.video_paused = False
            print("Cannot continue video: No video is currently playing")
        else:
            print("Cannot continue video: Video is not paused")

    def show_playing(self):
        """Displays video currently playing."""
        if self.currently_playing:
            if self.video_paused:
                print(
                    "Currently playing: " + self.currently_playing.title + ' (' + self.currently_playing.video_id + ') [' + (
                        ' '.join([tag for tag in self.currently_playing.tags if isinstance(tag, str)])) + '] - PAUSED')
            else:
                print(
                    "Currently playing: " + self.currently_playing.title + ' (' + self.currently_playing.video_id + ') [' + (
                        ' '.join([tag for tag in self.currently_playing.tags if isinstance(tag, str)])) + ']')
        else:
            print("No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
