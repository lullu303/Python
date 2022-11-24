def get_ans(ans):
    if ans in ['예', '아니오']: # [리스트] {사전} (튜플)
        print('정상적인 입력입니다.')
    else:
        raise ValueError('입력을 확인하세요.') 
        #예 또는 아니오 이외의 ans값이 있을 경우 valueError()라는 예외 객체를 발생시킨다.
    
    while True:
        try:
            ans = input('예/아니오 중 하나를 입력하세요 :')
            get_ans(ans)
            break
        except Exception as e:
            print('error: ', e) #예외가 발생하면 이 코드가 처리함