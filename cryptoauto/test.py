import pyupbit

access = "OcicXxKDx8apRByzLJZkrkeWaT3iJHZKnNxga5G2"          # 본인 값으로 변경
secret = "TzOJXGK8I02xCOQ4r2hni4PX5YD5kqHCKLaNxEan"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-ENJ"))     # KRW-XRP 조회
print(upbit.get_balance("KRW")) 