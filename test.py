import itertools



data = ['cách nạp tiền võ lâm truyền kỳ mobile',
'cách nạp tiền zing play',
'cách nạp tiền zingplay bằng tin nhắn',
'cách nạp tiền điện thoại viettel',
'cách nạp vcoin',
'cách nạp vcoin bằng sms',
'cách nạp vcoin bằng thẻ viettel',
'cách nạp vcoin bằng điện thoại',
'cách nạp vcoin cf',
'cách nạp vcoin qua sms',
'cách nạp vip chiến dịch huyền thoại',
'cách nạp xu bằng sms',
'cách nạp xu vào bang bang',
'cách nạp zing xu',
'cách nạp zing xu bằng sms',
'cách nạp zing xu bằng thẻ điện thoại',
'cách nấu',
'cách nấu cao mèo',
'cách nấu cua',
'cách nấu súp',
'cách nấu sữa bí ngô',
'cách nấu ăn',
'cách nằm trong truy kích',
'cách nối 2 màn hình vào 1 cpu',
'cách nối các vế câu ghép',
'cách nối dây quạt tản nhiệt',
'cách nối dây sạc điện thoại bị đứt',
'cách nối nhạc',
'cách nối wifi cho laptop',
'cách nổi tiếng nhanh trên facebook',
'cách oc cpu',
'cách offline facebook',
'cách out viber',
'cách out viber trên máy tính',
'cách out viber trên pc',
'cách parkour',
'cách parkour cf',
'cách perfect trong audition',
'cách pha nước làm lông mèo',
'cách pha pu',
'cách phi bài',
'cách phi bài mạnh',
'cách photoshop ảnh trên máy tính',
'cách photoshop ảnh tự sướng',
'cách phá khóa iphone 4',
'cách phá khóa iphone 5',
'cách phá khóa iphone 6',
'cách phá mã bảo vệ ngọc rồng',
'cách phá mã otp',
'cách phá mã otp cf',
'cách phá mã otp vtc',
'cách phá mật khẩu iphone',
'cách phá mật khẩu iphone 4',
'cách phá mật khẩu iphone 4s',
'cách phá mật khẩu iphone 5',
'cách phá mật khẩu iphone 5s',
'cách phá mật khẩu iphone 6',
'cách phá mật khẩu zalo',
'cách phá mật khẩu điện thoại',
'cách phá pass iphone',
'cách phá pass wifi',
'cách phát hiện camera',
'cách phát hiện camera quay lén trong khách sạn',
'cách phát hiện camera trong nhà nghỉ',
'cách phát hiện máy ghi âm',
'cách phát hiện máy ghi âm trong phòng',
'cách phát hiện máy nghe lén',
'cách phát hiện địch trong pubg',
'cách phát live trên facebook',
'cách phát nhạc qua loa bluetooth',
'cách phát phim trực tiếp trên facebook',
'cách phát triển tay to trong aoe',
'cách phát trực tiếp',
'cách phát trực tiếp fb',
'cách phát trực tiếp game trên facebook',
'cách phát trực tiếp trên face',
'cách phát trực tiếp trên facebook',
'cách phát trực tiếp trên facebook bằng máy tính',
'cách phát trực tiếp trên facebook bằng điện thoại',
'cách phát trực tiếp trên fb',
'cách phát trực tiếp trên iphone',
'cách phát trực tiếp trên pc',
'cách phát trực tiếp trên điện thoại',
'cách phát trực tiếp youtube trên facebook',
'cách phát video trực tiếp trên facebook android',
'cách phát wifi mạnh hơn',
'cách phân biệt iphone lock',
'cách phân biệt iphone lock và quốc tế',
'cách phân biệt ẩn dụ và hoán dụ',
'cách phòng chống wannacry',
'cách phòng ngự fifa online 3',
'cách phòng ngự trong fifa online 3',
'cách phóng to chữ trên màn hình desktop',
'cách phóng to màn hình desktop',
'cách phóng to màn hình laptop',
'cách phóng to màn hình youtube',
'cách phản xạ nhanh',
'cách phối',
'cách phối hợp quân trong clash of clan',
'cách phục hồi tin nhắn trên zalo',
'cách phục hồi tin nhắn đã xóa trên facebook',
'cách phục hồi tóc uốn bị cháy',
'cách ping',
'cách ping ip',
'cách ping kiểm tra mạng']
ssh = ['', '8123', '8124'] 



def batch_split(iterable, n_size):
    l = len(iterable)
    for ndx in range(0, l, n_size):
        yield iterable[ndx:min(ndx + n_size, l)]


def roundrobin(*iterables):
    "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
    # Recipe credited to George Sakkis
    num_active = len(iterables)
    nexts = cycle(iter(it).__next__ for it in iterables)
    while num_active:
        try:
            for next in nexts:
                yield next()
        except StopIteration:
            # Remove the iterator we just exhausted from the cycle.
            num_active -= 1
            nexts = cycle(islice(nexts, num_active))


def round(i1, i2):
    for i, j in zip(itertools.cycle(i1), i2):
        yield [i,j]



spl = batch_split(data, 5)
rr = round(spl, ssh)
print (rr)
for i in rr:
    print (list(i))
    print ('_____')