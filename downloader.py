import youtube_dl



class Videocapture:


    def video(self, link:str):
    # initial setting
        video = {}
    # ydl_otps = {'outtmpl': '%(title)s%(ext)s'}
    # to add more config parameter td

        # format_info={'format_code':[],'extension':[],'resolution':[],'format_note':[],'file_size':[]}
    # for GUI display

        ydl = youtube_dl.YoutubeDL()


    # object

        video = ydl.extract_info(link, download=False)
        return video, ydl
###another sort func tey to use hash to complete a better speeed
    # def sort(self, video):
    # # info sorted
    #     file_count = 0
    #     format_info = {'format_code':[],'extension':[],'resolution':[],'format_note':[],'file_size':[]}
    #     format_arry = video.get('formats') #foramt 是数组
    #
    #     if format_arry is not None:
    #         file_count = len(format_arry)
    #     for i in format_arry: # i 是dic
    #         format_info['format_code'].append(i.get('foramt_id'))
    #         format_info['extension'].append(i.get('ext'))
    #         format_info['resolution'].append(ydl.format_resolution(i))
    #         format_info['format_note'].append(i.get('format_note'))
    #         format_info['file_size'].append(i.get('filesize'))
    #     return format_info, file_count

    def sort(self, video):
    # info sorted
        file_count = 0

        format_code, extension, resolution, format_note, file_size = [], [], [], [], []
        format_arry = video.get('formats') #foramt 是数组

        if format_arry is not None:
            file_count = len(format_arry)

        for f in format_arry:
            format_code.append(f.get('format_id'))
            extension.append(f.get('ext'))
            resolution.append(f.get('format'))
            format_note.append(f.get('format_note'))
            file_size.append(f.get('filesize'))

        return format_code, extension, resolution, format_note, file_size,file_count

## test code
# v = Videocapture()
# a, b = v.video('https://www.youtube.com/watch?v=DpeO5AaDyHo')
# b.params = {'format': '18+251'}
# b.process_video_result(a)