package com.LinkedLists;

/**
 * Created by deepa on 6/29/2017.
 */
public class Song {
    private String songName;
    private Double duration;

    public Song(String songName, Double duration) {
        this.songName = songName;
        this.duration = duration;
    }

    public String getSongName() {
        return songName;
    }

    public Double getDuration() {
        return duration;
    }
}
