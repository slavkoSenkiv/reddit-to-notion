import re
string = """I just woke up to see I’m down $140 in the stock market today am I doing it right 😅 
444 17.02.21 DawsonBriggs  gnsno85
|   Just look at it upside down 
|   151 17.02.21 MemeElitist  gnsotvm
|   |   Move to Australia 
|   |   36 18.02.21 awzeus  gnugcyh
|   |   |   Lol. I’m from Australia and I’m down $595. 
|   |   |   28 18.02.21 aaykay13  gnvcrx0
|   |   |   |   Ure actually up 565$ 
|   |   |   |   4 18.02.21 Frankie1810  gnw7hiq
|   |   |   |   Down under? 
|   |   |   |   1 18.02.21 nitr04  gnxd6ya
|   At least you’re only down $140. At opening I was down like 3k. Still bleeding my eyes out in one account. *it is what it is*. Stonks only go up so it’ll be back to normal eventually if I don’t get margin called first 
|   43 17.02.21 notthediz  gnspl7q
|   |   Only 3k today? 
|   |   14 17.02.21 Godcranberry  gnsq0rw
|   |   |   Yup but now I’m back to about even since I’m expert stock picker. Speaking of passive income, I would be willing to sell you my stock picks if you’re interested >:)Edit: Lol looks like ppl couldn’t tell this was obviously a joke 
|   |   |   -22 17.02.21 notthediz  gnsqwtn
|   |   |   |   Can you teach me how to get margin called? 
|   |   |   |   3 17.02.21 Meatloaf451  gnto0u9
|   |   |   |   |   Open a margin account. Buy as many GameStop shares as you can afford 
|   |   |   |   |   -10 18.02.21 notthediz  gntyhih
|   |   |   |   It's okay man! Sure, how should we proceed? 
|   |   |   |   -2 17.02.21 Godcranberry  gnt2tk1
|   |   Why margin? 
|   |   2 18.02.21 Tubbytom8  gnu3n2t
|   The market is shit right now. It's a casino at this point. 
|   24 17.02.21 Givemeallyourtacos  gnsw0dv
|   |   Buying individual stocks is *always* a gamble, there's never a safe time doing that. Buying total market or S&P funds on the other hand is an incredibly safe investment that will make you a lot of money if you hold out for a long time. 
|   |   35 17.02.21 the_0rly_factor  gntha5y
|   |   |   what type of S&P funds do you think a 21 year old should buy? index funds or mutual funds? and how long do you think I should hold onto them? I plan on putting my $1200 stimulus check into S&P but just not sure which one to choose. 
|   |   |   10 18.02.21 BITTAH99  gntt7g4
|   |   |   |   VOO for S&P or VTI for total market index which gives a bit more diversication. 
|   |   |   |   13 18.02.21 the_0rly_factor  gntu47u
|   |   |   |   |   does more diversification with VTI mean a safer investment in the long run? 
|   |   |   |   |   2 18.02.21 BITTAH99  gnurvzy
|   |   |   |   |   |   VOO and VTI are 80% the same with the other 20% of VTI being those mid/small cap stocks that VOO doesn't have. Technically that means VTI will be more volatile, though it is more diversified. Performance wise, they have been nearly identical. I think VOO has done better over this past decade but it's such a small margin that you wouldn't really notice a difference. 
|   |   |   |   |   |   1 18.02.21 the_0rly_factor  gnvx2mr
|   |   |   |   |   |   |   ohh ok got u. i’ll do a little more research ofc but i think i’ll go with VOO. 
|   |   |   |   |   |   |   1 20.02.21 BITTAH99  go30vnn
|   |   |   |    Buy an index ETF.  ETFs have better tax efficiencies and are easy to trade in and out of.   Diversify into US and international 
|   |   |   |   3 18.02.21 FearlessGuster2001  gnu3cyi
|   |   |   |   |   VTI isn't an ETF? 
|   |   |   |   |   1 18.02.21 Redkg  gnuflo2
|   |   |   |   |   |   Yes it’s an ETF.   There are mutual funds that track indices but due to tax efficiencies index ETFs are better option 
|   |   |   |   |   |   2 18.02.21 FearlessGuster2001  gnufrly
|   |   |   |   |   |   |   would u rather recommend VTI or VOO from S&P? 
|   |   |   |   |   |   |   1 18.02.21 BITTAH99  gnurz52
|   |   |   |   |   |   |   |   VTI since it gives you exposure beyond the large caps of the S&P 
|   |   |   |   |   |   |   |   1 18.02.21 FearlessGuster2001  gnvs41h
|   |   |   |   |   |   |   What tax efficiencies do index ETFs offer in comparison? 
|   |   |   |   |   |   |   1 18.02.21 JustAnotherBAMF  gnxbebz
|   |   |   |   I'd go with VT. Get some international exposure all in one 
|   |   |   |   1 18.02.21 Swoleattorney  gnv70y4
|   |   |   |   Ark etfs and kensho etfs and $MOON.  You’re young.  Roll the dice. 
|   |   |   |   1 18.02.21 AberdolfLincler420  gnv9uwp
|   |   |   This is true! Cant argue with that 
|   |   |   3 17.02.21 Givemeallyourtacos  gntj59x
|   |   |   I’m currently invested in individual stocks... one of them being AMC, which was overly hyped not too long ago. Will definitely look into a VTI and add money to it monthly. 
|   |   |   3 18.02.21 Candid-Anywhere is OP gnu3lz1
|   |   |   |   Don’t forget about international. VT 
|   |   |   |   1 18.02.21 nearsingularity  gnv3xw6
|   |   |   |   |   What’s an international VT?? 
|   |   |   |   |   1 19.02.21 Candid-Anywhere is OP go1so3f
|   |   |   |   |   |   VT includes international companies.https://investor.vanguard.com/etf/profile/VT 
|   |   |   |   |   |   1 20.02.21 nearsingularity  go2irtp
|   |   |   |   |   |   |   Thank you!! 
|   |   |   |   |   |   |   2 20.02.21 Candid-Anywhere is OP go2lnrj
|   |   |   What do you classify as a long time?? Also, do you recommend putting money into something like a  VTI monthly, yearly, or just putting in a lump of money early on and letting it grow? 
|   |   |   1 20.02.21 Candid-Anywhere is OP go3atas
|   |   |   |   A long time is 20-30 years or more. Yes you need to contribute on a regular basis, that is what investing is. 
|   |   |   |   1 20.02.21 the_0rly_factor  go4ehh8
|   |   [always has been](https://i.imgur.com/iRtrBOr.jpg) 
|   |   6 17.02.21 DawsonBriggs  gnt8n4z
|   Ahaha $140 down! Just you wait when my GME goes back up I’ll see something other than 80% losses!!!! 
|   8 17.02.21 PigBeins  gnt0qu5
|   |   💎🤲😜 
|   |   10 17.02.21 DawsonBriggs  gnt8djw
|   |   |   We’re still going to the moon right.... right? 
|   |   |   0 18.02.21 PigBeins  gnv5nuz
|   That’s pretty normal for a $50k portfolio. You’ll see swings of $1k-$2k daily. That’s why there’s not even a point to checking it unless you’re rebalancing 
|   5 18.02.21 iwantknow8  gntv72g
|   You'll have to work even after death.LOL 
|   3 17.02.21 MisterCherno  gntgsqx
|   Just install the green theme 
|   3 17.02.21 Meloxian  gntqkyn
|   Well it looks like you’ll be working when your dead too. 
|   3 18.02.21 StonksGoUp31  gntu7kt
|   Healthy market actions. 
|   1 18.02.21 KeepinItPiss  gnv8h16
|   Holding Doge I see lol 
|   1 18.02.21 thedorkening  gnwg3ba
|   You are doing good. I'm down €3k today. 
|   1 18.02.21 beceladon  gnxlg42
I have a few Instagram community pages that I schedule posts on. Not quite passive, but takes up 8-12 hours of solid work per week for around £13k a month. Super easy to do/start/grow. I started in January 2020 and stumbled on it by accident. I wake up to PayPal telling me I've been sent money everyday.. mostly because prime US time (my demographic) is when I sleep. 
126 17.02.21 HereForInheritance  gnspihn
|   This is interesting. Who pays you though? Are you an influencer and promote products? 
|   51 17.02.21 ___PM_Me_Anything___  gnspzkk
|   |   For my pages, dog owners with personal accounts for their dogs pay me. It's usually for one of two reasons.* They want more followers/engagement for their dogs insta page.* They want to show off their dog just because.I don't do any adverts on the page or promote products. I currently do around 32 posts a day across the pages. The highest has 9/10 paid dog features a day, every two hours, from 6am to 11:55pm GMT. 
|   |   66 17.02.21 HereForInheritance  gnsrnlk
|   |   |   Wow that is some great income! Do you repost the posts and tag them in the decription? How long did it take you to reach where you are today? Would be genuinely interested in hearing more about this :) 
|   |   |   23 17.02.21 fortunedudd  gnsy5it
|   |   |   |   The previous person running the account was doing features for free. I bought the account for $1,000 at 36k. I monetized it immediately from there. It took around 6 months to go from £800 in my first month to over £7/8k. All the posts are pictures they chose to be features. The money is in upselling them packages such as 3 posts & 3 stories, or 12 posts & 12 stories.Most people tend to go for the 3 posts and 3 stories, 6 posts and 6 stories or the longer month campaign. The 3 post 3 story campaign is structured like this; Day 1: Post 1. Day 2: Story of Post 1. Day 3: Post 2. Day 4: Story of Post 2. Day 5: Post 3. Day 6: Story of Post 3. That way they get 6 constant days of engagement.The only running costs are the account (which can be built from scratch for £0), the scheduling software (£360 p/m) (which has a free version) and a online to-do list (£3 p/m) to plan/schedule the stories. 
|   |   |   |   45 17.02.21 HereForInheritance  gnt1km0
|   |   |   |   |   what's the software you use to schedule posts? 
|   |   |   |   |   6 17.02.21 teboblerone  gnto4ha
|   |   |   |   |   |   Hoot-suite PRO for £300 + VAT a year. It's decent, but I've had soooo many problems with them. They do offer a free account where you can schedule 30 posts at a time and connect up to 3 social accounts. Facebook Creator Studio recently had a revamp, so I may be going over there. 
|   |   |   |   |   |   8 18.02.21 HereForInheritance  gnvacw7
|   |   |   |   |   Where did you buy the account? 
|   |   |   |   |   4 17.02.21 likely-high  gnt3nhl
|   |   |   |   |   |   I fell into it, as my sister had that breed of dog. I spent 3 days trying to boost her account organically, gave up, then direct messaged the community account on Instagram asking how much it was for a feature. He said it was free, so I asked how much he wanted for it. 2 hours, $1,000 and an angry girlfriend later I had the account and started monetizing it. 
|   |   |   |   |   |   70 17.02.21 HereForInheritance  gnt4dcu
|   |   |   |   |   |   |   I applaud you 
|   |   |   |   |   |   |   7 18.02.21 jobbins  gntv7op
|   |   |   |   |   What's the name of the software? 
|   |   |   |   |   6 18.02.21 kushpvo  gnu4cof
|   |   |   |   |   |   If you mean the auto-scheduling software, Hoot-suite PRO for £300 + VAT a year. It's decent, but I've had soooo many problems with them. They do offer a free account where you can schedule 30 posts at a time and connect up to 3 social accounts. Facebook Creator Studio recently had a revamp, so I may be going over there. 
|   |   |   |   |   |   4 18.02.21 HereForInheritance  gnvae0m
|   |   |   |   |   |   |   Thanks a lot for the info 
|   |   |   |   |   |   |   2 18.02.21 kushpvo  gnvgwqf
|   |   |   |   |   Sounds like your doing great, I had the same thing going with some YouTube channels that were monetized making us good money and then 4 years later YouTube shuts us down for no reason, just says our content didn’t meet their tos, not saying that will happen to you but I’m always worried about being reliant on someone else’s marketplace. Your probably safe with dog content but I was doing outdoor and diy content. 
|   |   |   |   |   3 18.02.21 Henrik-Powers  gnuxrqk
|   |   |   |   |   |   I have a full time job, and just do this on the side. I started in January 2020 just before the big wave of Corona. It's been nice to have something to do during the lockdown. I strongly believe in never relying on anything where social media is your main source of the income. I could wake up and it be gone tomorrow.The only plus side is 100% of my posts are from paying users now, so there is no content issues. They all want their posts on the page. 
|   |   |   |   |   |   3 18.02.21 HereForInheritance  gnvak94
|   |   |   |   |   |   |   do u mean copyright issues? do u have ones? u mean when u find something worth posting, but it is not yours... 
|   |   |   |   |   |   |   1 13.03.21 slavko_senkiv  gqs1o2d
|   |   |   |   |   What are the prices for each package and how do you find people willing to pay? 
|   |   |   |   |   1 18.02.21 seochatter  gnu49ix
|   |   |   |   |   |   Packages start from £10 all the way up to £1,300 depending on what they want. The owners of this breed are pretty minted as a puppy costs between £2,000 and £8,000 each. I don't do any outreach. It's all organic. People message me asking for a feature and I send them the same copy and paste. 
|   |   |   |   |   |   3 18.02.21 HereForInheritance  gnvagdj
|   |   |   |   |   How do you price those packages? 
|   |   |   |   |   1 25.02.21 mangotease  goq1ne4
|   |   |   |   |   Hi, I know I'm late for the party but can I DM you? I'm thinking of buying an account which has a good number of followers and they're engaging as well. But I need support in monetizing it. 
|   |   |   |   |   1 15.08.21 fyrebrick  h90t79s
|   |   |   Wow. How did you get started? How did you even hear this was a possibility? 
|   |   |   3 17.02.21 illupvoteforadollar  gntaiy8
|   |   |   Super cool, could i drop you a pm? Ive got a few q's if thats ok 
|   |   |   2 18.02.21 Charmingly_Conniving  gnu2vda
|   |   |   |   For sure dude. 
|   |   |   |   1 18.02.21 HereForInheritance  gnvagk8
|   What’s a community page?? And how many followers do you need to start making money on insta? 
|   19 17.02.21 Candid-Anywhere is OP gnsprvu
|   |   So a community page is actually just community sourced content and is usually a specific niche (animals, beauty, cars etc). I now run a free community where I teach others to build their pages etc. When you start to make money very much depends on the specific niche, but you can start making bear money from 10k onwards. You can see where I mod for the Discord link. 
|   |   35 17.02.21 HereForInheritance  gnsrbgh
|   |   |   Just read this -I would love to join this community! :) 
|   |   |   4 17.02.21 tokyomooon  gnt66km
|   |   |   |   Where is the discord link? I couldn't find 
|   |   |   |   4 17.02.21 gjfarma  gnt86jy
|   |   |   Also would like the discord link :) 
|   |   |   4 17.02.21 ibicKz  gntjly7
|   |   |   Please tell us more 👍 Googling “Instagram community page” didn’t come up with anything for me. 
|   |   |   2 17.02.21 Tmmylmmy  gntb5vs
|   |   |   |   'Instagram Theme Page' is probably a more google-able term. Or /r/ThemePages 
|   |   |   |   4 17.02.21 HereForInheritance  gntcqz0
|   |   |   This sounds great can you dm me where to join? 
|   |   |   1 18.02.21 Confidence114  gnvwq8o
|   [видалено] 
|   5 17.02.21 None  gnsqvjo
|   |   Yup! 
|   |   3 17.02.21 None  gnsu4tz
|   This sounds amazing! I would love to chat more if you’re willing. 
|   2 17.02.21 tokyomooon  gnt60i3
|   Remindme! 2 days 
|   1 18.02.21 badkittenatl  gnu9707
|   |   I will be messaging you in 2 days on [**2021-02-20 02:24:13 UTC**](http://www.wolframalpha.com/input/?i=2021-02-20%2002:24:13%20UTC%20To%20Local%20Time) to remind you of [**this link**](https://np.reddit.com/r/passive_income/comments/lm1vnc/warren_buffett_says_if_you_dont_find_a_way_to/gnu9707/?context=3)[**7 OTHERS CLICKED THIS LINK**](https://np.reddit.com/message/compose/?to=RemindMeBot&subject=Reminder&message=%5Bhttps%3A%2F%2Fwww.reddit.com%2Fr%2Fpassive_income%2Fcomments%2Flm1vnc%2Fwarren_buffett_says_if_you_dont_find_a_way_to%2Fgnu9707%2F%5D%0A%0ARemindMe%21%202021-02-20%2002%3A24%3A13%20UTC) to send a PM to also be reminded and to reduce spam.^(Parent commenter can ) [^(delete this message to hide from others.)](https://np.reddit.com/message/compose/?to=RemindMeBot&subject=Delete%20Comment&message=Delete%21%20lm1vnc)*****|[^(Info)](https://np.reddit.com/r/RemindMeBot/comments/e1bko7/remindmebot_info_v21/)|[^(Custom)](https://np.reddit.com/message/compose/?to=RemindMeBot&subject=Reminder&message=%5BLink%20or%20message%20inside%20square%20brackets%5D%0A%0ARemindMe%21%20Time%20period%20here)|[^(Your Reminders)](https://np.reddit.com/message/compose/?to=RemindMeBot&subject=List%20Of%20Reminders&message=MyReminders%21)|[^(Feedback)](https://np.reddit.com/message/compose/?to=Watchful1&subject=RemindMeBot%20Feedback)||-|-|-|-| 
|   |   1 18.02.21 RemindMeBot  gnu99nr
Dividend stocks. I’m currently earning $940/month. The only work I do is monitor the investments. 
121 17.02.21 corey333  gnssqcg
|   Mind sharing the companies?? 
|   35 17.02.21 Candid-Anywhere is OP gnstbeu
|   |   I’m happy to.  GAB, USA, NLY, PFLT,ARR. Those are all funds, rather than individual stocks. Less risk that way. There is a very active dividend sub here. r/dividends. Good luck! 
|   |   101 17.02.21 corey333  gnsvo4m
|   |   |   What platform do you use? 
|   |   |   9 17.02.21 justinn_m3  gnsxqag
|   |   |   |   I use TD Ameritrade. Trades are free there. 
|   |   |   |   23 17.02.21 corey333  gnsy3qm
|   |   |   |   |   [видалено] 
|   |   |   |   |   17 17.02.21 None  gnt1y3o
|   |   |   |   |   |   I don't mind at all. I have about $80k invested in dividend stocks.  Due to Covid I had pulled most of my money out of the stock market, and put it in savings where was it earning virtually nothing. In January of this year I decided to put that money to work and began researching dividend funds  all of the funds I listed can be purchased for approximately $10 per share. My current yield on investment is approximately 10%. I reinvest all dividend payments so the value continues to grow 
|   |   |   |   |   |   38 17.02.21 corey333  gnt6xof
|   |   |   |   |   |   |   Did you need that money that you pulled out due to Covid or did you just get scared and pull it out? If it's the latter, you made a pretty big error there. Generally speaking, it is never wise to try and time the market. If you pulled out when the market started tanking in Feb/March and didn't reinvest until this January, you paid the opportunity cost of one of the best years in recent history - not to mention your money devaluing due to inflation. 
|   |   |   |   |   |   |   1 19.02.21 MarylandTerps  gnyprvs
|   |   |   |   |   |   |   Brilliant, good for you man 
|   |   |   |   |   |   |   1 24.02.21 None  gojdvy1
|   |   |   |   |   |   I've been reading up on dividends in my research of passive or semi-passive income. Depending on company share prices, and dividend yield percentage they probably invested somewhere around $150,000 - $250,000 to reach $940/mo. This is purely speculation based on several examples I've seen on how to reach a certain amount of dividends. It could be more, or it could be less. If he invested less money it's because the yield percentage is higher than 5%, which most investors deem to be risky. 3-5% yield percentage is the recommended margin to reduce risk as much as possible, or so I've learned. 
|   |   |   |   |   |   8 17.02.21 sicurri  gnt7fpc
|   |   |   |   |   |   |   Sicurri you raise a valid point. Thank you. potential dividend investors should be aware that higher yielding payouts are often riskier, however since I'm talking funds instead of individual stocks there's less risk. In my case I researched the dividend history of each fund before I invested, and I recheck each one on a weekly basis to make sure there are no changes. 
|   |   |   |   |   |   |   18 17.02.21 corey333  gntk5f8
|   |   |   |   |   |   |   |   From a learning standpoint, when one of your dividend investments changes in a negative way, what do you do?Do you sell and invest somewhere else or? 
|   |   |   |   |   |   |   |   3 17.02.21 sicurri  gntqhu0
|   |   |   |   |   |   |   |   |   Great question, sicurri. There is no stock answer for that question.  If the overall market is red I note it and move on. Since I only investment funds rather than individual stocks, if I see a prolonged downward trend and a fund I've invested in I’ll look at their holdings to see what's causing the drag. Journal is speaking if there's a major dip I see that as a buying opportunity rather sell like opportunity 
|   |   |   |   |   |   |   |   |   8 18.02.21 corey333  gnu81mb
|   |   |   |   |   |   |   |   |   |   Thank you. 
|   |   |   |   |   |   |   |   |   |   1 18.02.21 sicurri  gnumc82
|   |   |   Do these all pay monthly? Also what was your criteria for selecting these specific instruments? 
|   |   |   5 17.02.21 illupvoteforadollar  gntc9g5
|   |   |   |   Two of the funds I listed pay monthly however that wasn't among my criteria. Since I'm reinvesting the dividends the payouts don't matter to me at the moment. I sought funds where I would get maximum return for the least amount of money;hence my $10 per share target. I then looked at dividend payout, yield, and history. I only bought funds with solid dividend payout histories. 
|   |   |   |   8 17.02.21 corey333  gntme03
|   |   |    I looked into the first one GAB and it doesn’t look good. On the fund page it shows that the GAB fund targets 10% yield and it would include giving investor back the capital if not enough yield from the holdings.  So the amount we receive monthly might be eating into our capital. I also saw the fund price dropped over many years and never recovered back. In the 90’s it’s peak price is double the current price. Last year around March, it lost 53%. https://www.gabelli.com/funds/closed_ends/-111  “The Equity Trust maintains a 10% Distribution Policy whereby the Trust pays out to common shareholders 10% of its average net assets each year. This distribution is paid quarterly. The distribution rate is not representative of dividend yield or the total return of the Fund and may include a return of capital.” 
|   |   |   3 18.02.21 ttkk1248  gnwgtv7
|   |   |   |   Thanks for that.  Of my fund picks, GAB is the one I’ve been least confident in. I’m still green there,but I may liquidate and move those funds elsewhere. 
|   |   |   |   0 19.02.21 corey333  gnyceu8
|   |   |   |   |   Ok I just also looked at another one on your list NLY. Management fee is 1+%, while earning per share is negative!I also found this description below on https://1.simplysafedividends.com/annaly-capital-management-nly/.   Your list of investments seem troubling. Please stay safe. Stick with something like Vanguard or join r/Bogleheads to learn more on long term investment before losing your shirt.“Unlike equity REITs, which generate stable rental income from leasing out physical real estate properties, mREITs like Annaly should be thought of as financial companies. They own no permanent assets, but rather operate purely on the basis of interest rate arbitrage, profiting from differences in interest rates on various assets. The firm’s assets eventually mature and must be replaced, meaning that mREITs like Annaly have extremely volatile revenue and earnings over time. In addition, mREITs are among the most interest rate sensitive companies in America. This is because Annaly’s main funding source is the repurchase, or repo, market. For this type of financing, Annaly sells some of its assets in order to raise funds, promising to buy them back at a slightly higher price in a few weeks (usually 14 to 72 days).” 
|   |   |   |   |   3 19.02.21 ttkk1248  gnyhlb3
|   |   |   What is USA? There seems to be some ambiguity when looking for it online. 
|   |   |   1 18.02.21 CandidConvo4  gnuxnii
|   |   |   |   Look for Liberty All Star Equity Fund. 
|   |   |   |   1 18.02.21 corey333  gnw0b1k
|   |   |   Nice list. 
|   |   |   1 21.02.21 joellecool  go7axop
|   How much did you invest to get to that level per month? I'm only sitting at around 10-20$ per month but I'm looking to expand that 
|   7 17.02.21 Rj17141  gntcw3k
|   |   I reinvest all my dividends. Compound investment is your friend. 
|   |   12 18.02.21 corey333  gnu8o2n
|   Me too! And I love it! 
|   1 18.02.21 Blair-Dyson  gntwahl
|   You sleep during market hours? 
|   1 18.02.21 AnUninterestingEvent  gnuv7dd
|   |   Markets are open all day as long as you don't limit yourself to 1 exchange 
|   |   2 18.02.21 RuthBaderBelieveIt  gnvg0kk
|   Look into $QYLD. NASDAQ covered call etf that pays around ~12% /year with dividends paid out monthly 
|   1 18.02.21 d4ng3rz0n3  gnvcaci
I let people use my unconscious body for sex while I sleep. I wake up to a dresser littered with quarters. 
87 17.02.21 goatsandhoes101115  gnszrfs
|   Wait what 
|   16 17.02.21 Allergies-Feminists  gnt2jxx
|   |   Yes? 
|   |   9 17.02.21 goatsandhoes101115  gnt35df
|   |   |   You might be trolling but just in case how do you monitor that 
|   |   |   11 17.02.21 Allergies-Feminists  gnt8id9
|   |   |   |   Easy, I have a webcam rolling the whole time. That way I can make sure everyone is leaving their quarter (and not stealing quarters) AND I charge peeps to watch the live stream. The old two birds with one stone. 
|   |   |   |   8 18.02.21 goatsandhoes101115  gnu53vk
|   |   |   |   |   Wow. Your really smart. Or at least smarter than me. How did you come up with this? 
|   |   |   |   |   2 18.02.21 Allergies-Feminists  gnu8r2s
|   |   |   |   |   |   Hoho I sure hope you're smarter than me! I almost feel like I should dump all these quarters into a full time baby sitter just to make sure I'm not trying to eat soup that's too hot or drown in the shower because I forget to close my mouth. 
|   |   |   |   |   |   6 18.02.21 goatsandhoes101115  gnu9vqx
|   |   |   |   |   |   |   Lmao. Also do you not wake up when you’re being.... 
|   |   |   |   |   |   |   3 18.02.21 Allergies-Feminists  gnuar4y
|   |   |   |   |   |   |   |   I'm not the heaviest sleeper but my "male-box" is extremely accommodating so the clients doodle usually isn't enough to ping on my radar. 
|   |   |   |   |   |   |   |   2 18.02.21 goatsandhoes101115  gnvr5tv
|   |   |   |   |   |   |   |   |   Wow well i wish you the best with your side hustle 
|   |   |   |   |   |   |   |   |   1 19.02.21 Allergies-Feminists  go15uss
|   I read the title and thought this is what WB must have meant.1. Find buyers by posting on CL, pornhub, fansonly, or some subreddit offering sex with sleeping body.2. Go to sleep3. ???????4. PROFIT!You'll either wake up with money or die (without having to work until you die). Win-win! 
|   3 18.02.21 zxc123zxc123  gnxfxfq
|   |   Can somebody explain this in details please ? 
|   |   1 23.02.21 ahmed997  goho7v4
Just starting out with crypto and stock market. Need to really find more ways to grow my money. 
48 17.02.21 Twisting-Nips  gnspnjr
|   Same... minus crypto. I’m still on edge about it.. though I’ve been hearing a lot about doge coin. I just can’t tell if it’s a joke or not 
|   18 17.02.21 Candid-Anywhere is OP gnspzh8
|   |   Doge is literally a joke, it was made to be a funny 
|   |   76 17.02.21 gambits13  gnstlqe
|   |   |   And yet it does the same thing as a bitcoin 
|   |   |   5 18.02.21 MCP1291  gnwnfxp
|   |   |   |   except it's not secure.  I don't think it has quite as many miners as bitcoin.  Which means it can be 51% attacked, and should not be taken seriously. 
|   |   |   |   1 18.02.21 gambits13  gnwnscz
|   |   |   |   |   That’s like putting securing pocket lint at Brinks and saying this lint is more valuable bc it’s secure. It’s just numbers on a screen. 
|   |   |   |   |   2 18.02.21 MCP1291  gnwt7c2
|   |   |   |   |   |   Huh?  No.  That analogy makes no sense.  I don’t think you understand what security means for a crypto currency.  Security for a crypto refers to not allowing the numbers to be manipulated or double spent.  A 51% attack would allow an entity to manipulate the “numbers on the screen.”  If you can do that, then you can spend the same -insert currency here- twice, rendering it useless.  It’s nothing like putting pocket lint in a brinks at all.So the difference between doge and btc is mainly security, and that’s worth about $51,000 to the market. 
|   |   |   |   |   |   2 18.02.21 gambits13  gnwvlw3
|   |   |   |   |   |   |   I understand that. I’m saying the argument that bitcoin is better than doge is semantics. They’re both equally numbers on a screen and nothing more. They’re valueless. 2 strands of Lint are essentially valueless. Lint in a brinks vault makes it more secure. That doesn’t add any value to it. That’s what the crypto ppl miss and why they’ll ultimately suffer the same fate as GameStop All unbacked Cryptos are equally fiat nothing(Even lint has some value as a fire starter) 
|   |   |   |   |   |   |   1 18.02.21 MCP1291  gnwx0f9
|   |   |   |   |   |   |   |   Eh, maybe maybe notThe dollar bill is just as valuable as that piece of lint.  The only difference is the dollar is backed by the guns of the US govt that say you have to accept it.A medium of exchange or store of value that doesn’t have to be backed by guns, and instead can be universally agreed upon might be viewed as a different alternative to some people.  Maybe your views are antiquated and you should open your mind to new technologies and systems, maybe people aren’t as trusting of governments as you.Or maybe all this magic internet money will collapse and go to zero, that’s probably more likely than a non govt crypto becoming a world reserve currency as some people speculate.Either way, there is still a difference between BTC and doge.  And security does have value to some people, regardless of if it has value to you or not.You aren’t the first person to say it’s worthless, and you certainly won’t be the last.  I can’t believe BTC is valued at 50k+ and I strongly believe it’ll correct, but if it has value to some, then it has some value.  No idea what that is though 
|   |   |   |   |   |   |   |   2 18.02.21 gambits13  gnwz8al
|   |   |   |   |   |   |   |   |   You’re absolutely right about the dollar and the threat of government being the backingThe point is your jumping out of the frying pan and into the fire. Going from fiat to fiat. Money needs to have an end user for it to have value AND be money 
|   |   |   |   |   |   |   |   |   1 18.02.21 MCP1291  gnwznef
|   |   The only thing giving doge its value is Elon musk tweeting about it. With the absurd amount of doge coin in existence and how many can be mined is cray cray, but who knows maybe I'm wrong 
|   |   29 17.02.21 Megalennie1  gnsqnpt
|   |   Doge coin is a meme that pumps and dumps.  It's a casino not an investment. 
|   |   22 17.02.21 ClassyDumpster  gnsrzbf
|   |   |   Doge !! is falling don't who who is selling also the sub-reddit /doge is gone mad they are soo crazy to tell everyone to hold the coin 
|   |   |   1 18.02.21 shubham_2009  gnvfas5
|   |   I think the doge coin started as a meme coin but it seems to have grown quickly then died out and then Elon dropped his tweet and it blew up again. Don’t invest in meme crypto though unless you are going to hold for the long haul. Etherum seems to be the one that is blowing up at the moment. But it’s all a mystery to me 😂 I’m just in the staking crypto because it’s easy. 
|   |   5 17.02.21 Twisting-Nips  gnsrqj3
|   |   If you invest in crypto there is tons of ways to make money, I hold 1100 Cardano ADA  it pays 5% per year but you get your rewards every four days wich makes a nice compound interest. Also the value of cardano will likely go up (just a guess) but since I invested my money almost quadrupled, but I want to build a decent stash so I just keep buying each month.You can also stake DOT on the polkadot network for about 12% and KSM on the Kusama network for about 16% here you have the same effect you get your staking rewards regularly every 7 days I think, and it just ads more to the amount staked.You can stake BNB on Binance to earn rewards you van just stake your usdt for 6% a year thats not even that risky unless they get hacked...There is also an indexfund for crypto on bitpanda, also Canada just listed a bitcoin etf I can send you invites to bitpanda and you get a 10€ bonus after your first trade.I also invested in the defi pulse index which replicates the value of the top ten decentralized finance tokens.That made a solid 110% in the last month.But be careful the more you are moving around in this space the less you will sleep. I only invest what I can afford to loose and I invest for the long term I really love it when all rush to sell of their crypto, I just buy more when the price dipsGoodLuck! 
|   |   5 18.02.21 Photo_film_  gntz3a9
|   |   |   I am also holding cardano!! But I don't get any rewards also what is the KSM network I was passively investing in coins before so I don't know that can you please elaborate. 
|   |   |   1 18.02.21 shubham_2009  gnvf83a
|   |   It IS a joke, however it seems that Musk is at least semi serious in his doge endorsement which IMO is an insult to the crypto community. 
|   |   1 18.02.21 Crustybrown  gnu29ei
|   |   Oh my God do not buy doge. Its literally a joke 
|   |   1 18.02.21 king_dingus92  gnvkj87
|   |   DO NOT BUY DODGE COIN. Literally it’s a pump and dump going on right now. dodgecoin was never meant to be more than 0.0001 USD imo. Also there is no supply limit to the amount of dodgecoin and there are currently more than 100billion. 
|   |   1 18.02.21 -Jive-Turkey-  gnw6w37
i make video overlays and sell them as a digital download.  i make anywhere from $30-$60 a day (i've had a handful of $100 days, but those don't happen very often).  it takes a few hours to make them, but once they're done, i literally don't do a single thing other than watch payments come in.  i try to make a new overlay each month. 
47 17.02.21 reddikan  gnt6zu7
|   What are these? Backgrounds that overlay the video? 
|   9 18.02.21 allboolshite  gnui9vx
|   |   not really backgrounds.. they’re overlays. mainly light leaks/old film burn overlays 
|   |   5 18.02.21 reddikan  gnwwfpd
|   |   |   I don't understand. Would you link an example? 
|   |   |   3 18.02.21 allboolshite  gnxb15i
|   Very interesting! Where do you sell them? 
|   4 17.02.21 Jimboy10  gntiq0a
|   |   i upload all of my overlays on youtube and drive the traffic from there to my sellfy site! 
|   |   8 17.02.21 reddikan  gntkhuu
|   What site do you sell on? 
|   1 18.02.21 Rooster-chan  gnx1baf
|   |   i looked at the pros and cons between sellfy and shopify and decided to go with sellfy.  i couldn't be happier with them! 
|   |   4 18.02.21 reddikan  gnx6ani
|   Cool idea. I could do this openly at work due to my job. Where do you upload them, if I may ask? 
|   1 06.06.21 Rauchgestein  h0u5nv9
Rental property... I make money while other people sleep. 
42 17.02.21 deserttrends  gnsvlz9
|   That's something a thief would say too. 
|   14 18.02.21 HumbleWarriorr  gnvkira
Falling asleep at work 
41 18.02.21 sAvage_hAm  gnuuypz
Invest passively in real estate. To be clear, passive investing in RE isn’t owning your own property. 
35 17.02.21 Untzthyme  gnstf6w
|    Could you elaborate on not owning your own property, but investing in real estate 
|   14 17.02.21 Candid-Anywhere is OP gnstk25
|   |   Sure, I prefer investing through real estate syndications but if you have less capital, platforms like crowdstreet are fine 
|   |   12 17.02.21 Untzthyme  gnstosg
|   |   |   Are you talking about REITs ? 
|   |   |   7 17.02.21 philipjfrizzle  gnsynpa
|   |   |   |   No, REITs typically have lower returns and no tax advantages 
|   |   |   |   1 17.02.21 Untzthyme  gnsyq4l
|   |   |   |   |   Looking thru crowd street.. these aren’t REITs? What type of investments are these? 
|   |   |   |   |   4 17.02.21 philipjfrizzle  gntderg
|   |   |   |   |   |   REITs are a pool of properties, typically on crowdstreet you’re investing in an individual property 
|   |   |   |   |   |   7 17.02.21 Untzthyme  gntdn0m
|   |   |   Sorry but how do real estate syndication work and how do they differ from crowd street or REITs? 
|   |   |   5 18.02.21 reelznfeelz  gnu2t6y
|   |   |   |   REITs are a pool of properties and have no tax advantagesCrowdfunding is similar to syndications but you’re typically getting syndicators worst deals when you go through platforms. These platforms charge fees to the syndicators and if deals are good, theyll fill up without using a platform. When you go straight to syndicators you’re going right to the source and you’re not getting their worst deals 
|   |   |   |   3 18.02.21 Untzthyme  gnu345m
|   |   |   |   |   If you don't mind me asking, what are some of the tax advantages of using syndicators / other group real-estate? How much is a minimum / average investment? 
|   |   |   |   |   3 18.02.21 HeroCC  gnuum7h
|   |   |   |   |   |   REITs are taxed as regular incomeSyndications are taxed as passive income with k1 documents so they’re typically going to be tax free thanks to depreciation and bonus depreciation.A typical syndication minimum is 50-100k but I’ve seen as low as 5k 
|   |   |   |   |   |   3 18.02.21 Untzthyme  gnux2ar
|   How are the returns, and what is the worst part? 
|   5 17.02.21 Rusty_Shacklefurd69  gntj3mh
|   |   The returns I typically see on the platforms are 6-8%, but can get over 10% on high performing deals. I prefer investing through syndications, typically a syndication deal will end up on a platform if they can't do the raise themselves, so you're potentially getting more bottom barrel type deals there. If you have the capital, you're likely better off going straight to the syndications. 
|   |   7 17.02.21 Untzthyme  gntjjwe
|   |   |   Interesting. What's the investment lock-up period on something like this, and what're the downsides/biggest risks? 
|   |   |   1 17.02.21 Rusty_Shacklefurd69  gntjtmm
|   |   |   |   Varies, you'll likely see some as low as 3 years and as long as 10 years. Risks will depend from asset to asset. Multifamily biggest risk will be covid return/eviction moratorium. Biggest risk of office space is people not returning to work. Biggest risk of strip mall is places going out of business. Etc. It's at least backed by a hard asset though so the likelihood of your investment going to zero are very low. 
|   |   |   |   3 17.02.21 Untzthyme  gntkf3o
|   |   |   |   |   Thanks for sharing man. Got some cash that I'm looking for some alternative investments for. Can you share who you use? 
|   |   |   |   |   2 18.02.21 Rusty_Shacklefurd69  gntuym1
|   |   |   |   |   |   Just messaged you. Not trying to advertise anything here 
|   |   |   |   |   |   5 18.02.21 Untzthyme  gnu10gj
|   |   |   |   |   |   |   I'd be curious too if you don't mind a PM.   We were planning to buy properties to manage but honestly after looking into it, it's looking like just way too hands on and time intensive for the returns you'd get.  I have a day job and simply don't have the mental energy to go spend 4 hrs after work every day laying flooring, painting and doing drywall.  That sounds miserable.  However, we have money just sitting around not doing anything and need to do something with it before long. 
|   |   |   |   |   |   |   1 18.02.21 reelznfeelz  gnu39rx
|   |   |   |   |   |   |   |   Yep I feel your pain. Incoming.. 
|   |   |   |   |   |   |   |   1 18.02.21 Untzthyme  gnu3crt
|   |   |   |   |   |   |   |   |   I'm also interested if you don't mind. I was not aware of this re route. Thank you for being open about this. I 
|   |   |   |   |   |   |   |   |   1 18.02.21 Earl-of-Jabroni  gnu9jhq
|   |   |   |   |   |   |   |   |   |   Sent 
|   |   |   |   |   |   |   |   |   |   1 18.02.21 Untzthyme  gnu9sys
|   |   |   |   |   |   |   |   |   I’d also love some more info. I appreciate the advice! 
|   |   |   |   |   |   |   |   |   1 18.02.21 mountaingoatsclimb  gnw7wvv
|   |   |   |   |   |   |   |   |   |   You got it 
|   |   |   |   |   |   |   |   |   |   1 18.02.21 Untzthyme  gnwa9cx
|   |   |   |   |   |   |   |   I’m also interested if you don’t mind! I’ve heard about this kind of investing in real estate, but don’t know anything about it or where to look, so it’d be much appreciated! 
|   |   |   |   |   |   |   |   1 18.02.21 119-Vicious  gnx8f3g
|   Is it kinda like the app fundrise? 
|   3 18.02.21 xoxobenji  gnu360b
I think he is the one still working at 90, while many folks who just worked 9-5 are enjoying retirement life.Just an observation, Buffet fans pls don't crucify me for this 😋 
36 17.02.21 testuser150  gntg2uh
|   Buffet only ‘ works’ because he loves it. My grandma is 89 and still works everyday. Does she need to? No. She told me ‘ if I stop moving I’ll die’ pretty unnerving to think about tho 
|   18 18.02.21 Construction_Man1  gnuq3pv
|   Fair but he also has enough money to never work another day in his life while also allowing like 100 generations of his family after him to never have to work a day in their lives 
|   12 18.02.21 hotnrdy  gnud2re
|   The difference is choice vs necessity 
|   2 06.08.21 Madcat_Moody  h7xqevf
Low six figures from rental properties. 
30 17.02.21 csp256  gnspenp
|   low five figures for me.  Take that! 
|   24 17.02.21 gambits13  gnsu0ik
|   |   I live in a rental property. How bout dat! 
|   |   50 17.02.21 _some1one_  gnt4zom
|   |   |   we got a winner. honestly, rent is the way to go in most populated areas. 
|   |   |   8 17.02.21 rickety_rick  gnthnzg
|   |   |   |   lol? 
|   |   |   |   1 17.02.21 csp256  gntkaby
|   You must've invested long ago? + might have good paying job and probably in 30s or 40s? Nothing, jus curious to calculate stuff to think Accurately 🙌 
|   2 27.02.21 SSV-LEGEND  gozsryf
|   |   I bought my first house 2 years ago. It was $635k and bought with 5% down. Yes I have a high paying job (research engineer at a FAANG), but I was earning about half what I do now when I bought that first house. I'm 34 but I only started my professional career at 30 because I was a non traditional student. Most of my properties are out of state and have gross rents of 2% of acquisition price per month. 
|   |   2 27.02.21 csp256  gp2zhf7
|   |   |   Why didn't you buy with 20% down payment? As its wiser to use bank's money than urs as interest rates were lower & inflation is off charts? 😒 
|   |   |   1 01.03.21 SSV-LEGEND  gpacr8i
|   |   |   |   Inflation was not high when I bought, it was very low. Also, even this year's inflation is not very high historically (see the Volcker era).But in general the total return of that house (that investment) was significantly higher than the interest payments, and the rental income was quite low volatility so leveraging up makes quite a lot of sense for a young investor in their accumulation phase. Paying off properties is not actually the goal, and I will in fact refinance my portfolio to keep my leverage sufficiently high.You may be interested to know that the return on equity (ROE) of an investment which returns R unlevered, but is financed at a rate of r is:    ROE = (R - r*x) / (1 - x)Where x is the fraction of the investment which is financed. This is ignoring risk, of course, but it generally shows why debt can be attractive. [Consider this image, too.](https://imgur.com/AbLL4ec) 
|   |   |   |   2 01.03.21 csp256  gpbvcjy
I’ve been crypto-mining for the past couple days. 3 days worth ETH mining and I made $90 USD with only 3 GPUs. I have 6 total GPUs so my estimated income should be around $1.5k-$1.7k a month depending on the price of ETH.But other passive income streams I have is my Esty store where I sell printables. I make them once, set, and forget. I make around $60 USD a month but could be way more profitable if I actually put effort into it. I only have around 10-12 printables to sell in my shop.EDIT: Since the time of writing this, I have 13 total GPUs now (total investment is $8.4k) and I just ROI’d as of a May 3rd 2021. 
25 17.02.21 Yiggah  gnt8myi
|   How much was your start cost on crypto mining? 
|   6 17.02.21 PatientHusband  gntgr1y
|   |   My graphics card were all purchased at MSRP, right now mining is very hot because you’re making really good profit margins since it’s a bull market. Everyone and their mother wants a GPU for gaming and also mining so it’s extremely difficult to purchase. My rig so far consists of:2 x RTX 3080, 3 x RTX 3070,1 x RTX 3060ti,12 GPU risers,1200watt Platinum Efficiency server PSU,DIY Rig,Cheap Monitor,PCIE WiFi6 Adapter,3x 120mm FansAnd other miscellaneous items came out to around $4k. I’m estimating to make it all back in 2.5 months as ROI. But it could be sooner since ETH is rising daily. I’m not concerned about the risk as I can turn around and sell the cards for 1.5x value since they are going for around 2x the price of MSRP due to low supply and high demand. 
|   |   13 17.02.21 Yiggah  gnti0s8
|   |   |   How’d you learn how to do this? 
|   |   |   6 18.02.21 PatientHusband  gnu5osm
|   Wow, did not realize mining was still a real thing. I'm way out of the loop, but please share more info if you feel like it. How much is your equipment, how involved is mining, etc. Thanks! 
|   2 17.02.21 toughinitout  gnth5x1
|   |   See above comments. ;) 
|   |   3 18.02.21 Yiggah  gnwih53
|   What kind of printables do you make? Did it take a lot of work for you to start generating sales, or did they just roll in? 
|   2 18.02.21 thehellcat  gntwdnv
|   |   It took a couple days but I focused more on quality than quantity. One of my best seller is a birthday printable. 
|   |   2 18.02.21 Yiggah  gnwhkqr
|   |   |   How different is etsy from shopify? I know that for shopify you create your own store then have to advertise it, and the advertising cost can really make you lose money, but seeing as how your making 60$, I assume your not advertising? Also, could you possibly link your store so that I can get an better idea as to what products you sell? Thanks in advance! 
|   |   |   1 18.03.21 Blessedman11  grbyk3s
|   Can you tell how should I start to mine the ETH and what are other crypto that would pay me to mine thanks!!! 
|   2 18.02.21 shubham_2009  gnvfy42
|   Was just going through older posts on the subreddit. Guess that's worth a bit more now 
|   2 05.05.21 Madsmathis  gx1sael
|   |   Haha yeah I just ROI’d on my investment. Started mining in Feb of 2021 and as of a couple days ago when ETH hit 3.4k (ATH), I hit my ROI which was 8.4k. Any mining from now is just pure profit + icing in the cake is the resale of the GPUs which is probably worth 10-15k. 
|   |   1 05.05.21 Yiggah  gx1szxj
|   Have you factored electricity costs into that? 
|   1 18.02.21 respeckKnuckles  gnwh80s
|   |   Yes, electricity is pretty negligible. I have a energy tracker plugged into the wall. In my 6 days of mining (only three cards, waiting for my PSU to come in to power the rest) I’ve used around 87kWh. In my area, I pay .07 cents per kWh so far I’ve paid $6.09 for the 6 days. I’ve made $90 + $64.17 = $164.17 - $6.07 = $148.01 net profit at the time of writing this post. I can then hold the ETH and hope it continues to go up in price or I can cash out now and get it in USD. Another way to make more money is to deposit your ETH into BlockFi which is like a high yield savings account for crypto. I think ETH earns around 5.5% annually. 
|   |   2 18.02.21 Yiggah  gnwic2u
Crypto currency.  I started a little over a year ago with 18k. I'm at 160k now. 
26 17.02.21 ClassyDumpster  gnsqa6i
|   That's nice man, I never understand how people make profit with crypto. Do you mind sharing any ressources you'd find interesting to consume concerning getting into crypto? 
|   7 17.02.21 dankvald  gntq76b
|   |   Crypto is just like stocks. Find the good ones and hold them. I bought bitcoin at 14k and watched it drop to 4k. I just kept buying and holding. 
|   |   9 18.02.21 ClassyDumpster  gntwm4i
|   |   [видалено] 
|   |   5 18.02.21 None  gnvctqa
|   |   |   I'm on Binance, So I went for btc, ada and xml ! 
|   |   |   3 18.02.21 dankvald  gny0ynm
|   Can you withdrawal the money at any time? What happens when banks start releasing their own crypto and all the ones that were hyped up go bye bye. That really scares me. 
|   2 17.02.21 Candid-Anywhere is OP gnsqfm8
|   |   Yes you can withdrawn or sell at any time.  Crypto market never closes unlike stocks.  The major reason for some crypto is to take power away from banks.  There is a banker coin that does ok and isn't well liked. 
|   |   10 17.02.21 ClassyDumpster  gnsqwnu
|   Which coins 
|   3 17.02.21 clebux  gnsqy9r
|   |   What do you mean? Which do I have? 30% into bitcoin, 30% eth, 10% chainlink, 10% vechain, 5%xrp, 5% cardano and a few others. 
|   |   7 17.02.21 ClassyDumpster  gnsrbrt
|   |   |   Yup, thank you! 
|   |   |   1 17.02.21 clebux  gnsre9o
|   |   |   |   Make sure to do your own research! 
|   |   |   |   6 17.02.21 ClassyDumpster  gnsrgvb
|   |   |   |   |   What app do you use for your wallet, or do you use a physical crypto wallet?I'm interested in playing with crypto a bit, but my trading app doesn't support crypto and fuck if I'm letting Robinhood into my pocket again. 
|   |   |   |   |   1 17.02.21 Bookislovakia  gnszs5w
|   |   |   |   |   |   I use binance.us for buying and ledger for a hardware wallet. 
|   |   |   |   |   |   4 17.02.21 ClassyDumpster  gnt4ecy
|   |   |   |   |   |   |   Thank you! 
|   |   |   |   |   |   |   1 17.02.21 Bookislovakia  gnt4gi0
|   |   Stellar Lumens have been profitable for me and have a solid future.  Though you'd have made money on almost any crypto if you held over the last few months. 
|   |   7 17.02.21 imnos  gnsuhq9
|   Are you trading or just holding? 
|   1 17.02.21 fortunedudd  gnsyf85
|   |   Just holding,  I've lost money when trading lol 
|   |   1 17.02.21 ClassyDumpster  gnt4gy6
Crypto for me too.  Highly recommended.XLM and ADA have been great investments. 
21 17.02.21 imnos  gnsud3a
|   Variety is the spice of life. Don't spend it all on one hooker and one coke dealer. 
|   7 17.02.21 DeepSlicedBacon  gntguwg
|   |   Coke? Its 2021! I'll be microdosing psilocybin with the hookers. 
|   |   9 17.02.21 imnos  gnth98x
|   |   |   Well... La Di Da Mr French tickler. 
|   |   |   3 18.02.21 DeepSlicedBacon  gnua1sk
|   I like algorand a lot, plus you get between 6% and 8% APY depending on if you keep in the official wallet or Coinbase. 
|   2 18.02.21 SnooMachines6509  gntxhu5
|   |   Is it like staking? I do that with ADA, 5% yearly returns. 
|   |   1 18.02.21 deinterest  gnvcb5v
|   |   Do you get the APY if you buy some on Coinbase? Or is it strictly for the official wallet? 
|   |   1 20.02.21 Hefty_Goose_8000  go4jcbr
|   |   |   You get 6% on coinbase 
|   |   |   1 21.02.21 SnooMachines6509  goa3umk
|   |   |   |   Okay I see. Thanks for the reply 🙏🏻 
|   |   |   |   1 22.02.21 Hefty_Goose_8000  gob2xrv
|   |   Sorry but how does APY work? 6-8% APY how much that would be? I always have difficulties understanding them bcuz i was shit in maths ;/ 
|   |   1 27.02.21 SSV-LEGEND  gozsam2
I sleep naked and stream it on my onlyfan account 
20 17.02.21 FireLama  gnt8q4y
|   I reckon this is sounds like a solid idea. 
|   3 22.02.21 vialine  gob8lwf
|   Nice :) lie 
|   0 18.02.21 shubham_2009  gnvg4fu
Working on a children’s books to sell on Amazon 
20 17.02.21 captainvaughn  gnt24ie
|   Illustrated? 
|   1 18.02.21 Dexeh  gnwpo7p
|   |   Yeah a buddy of mine is a killer graphic designer so I’ll be using some of his skills. 
|   |   2 18.02.21 captainvaughn  gny3e05
|   |   |   Awesome! So do you split the profits? My wife is eyeing the self-publish route but would want to collaborate with someone who can draw. 
|   |   |   1 18.02.21 Dexeh  gny41ui
|   |   |   |   Yeah, I’m looking to give him $5 per illustration up front & a 20% royalty/commission on all future profits. 
|   |   |   |   1 19.02.21 captainvaughn  gnyuzov
Ebay. I think people with insomnia shop on there. 
14 17.02.21 foxpoint  gntb30b
Google "sleep stream", you literally making money while you sleep (or not). 
10 17.02.21 cryin-machine  gnt29kj
|   It's very much the or not part of your sentence. In order to do a sleep stream or slumber stream you have to already have existing followers, or just be female in order to make any money, if at all. 
|   8 17.02.21 sicurri  gnthcf6
|   |   Couple point/counterpoint here:* "just be female" - check out Asian Andy :)* "already have existing followers" - i agree this is very true, but it also bring out the larger and more fundamental point which is in order to start some sort of passive income stream that people suggest here (stocks, real estate, etc), you need some kind capital (money, followers, skillset etc). I saw people suggest investing in real estate but no one comment "hey you need money to do that". :)Also i was half joking about sleep stream since we are talking about making money while you sleep lol 
|   |   5 17.02.21 cryin-machine  gntiqqa
|   |   |   Female, or be cute in some capacity to someone. Investing capital is far easier than getting followers as humans are far more finicky than if you were to just throw money out into the world. However I mostly agree with you, lol. 
|   |   |   4 17.02.21 sicurri  gntj2ng
Diversified investments. For the sleeping part: investments in crypto currency. 
7 17.02.21 gcej1234  gntc20j
Holding GME like a boss! :-) 
8 18.02.21 densch92  gnvpm50
You might think I'm crazy but last year showed me: VHS Tape Glitches 
6 17.02.21 chick0rn  gnsvbdh
|   What is this? These words are in an order but arent making sense to me lol 
|   19 17.02.21 Papa_Pazuzu  gnswwjb
|   |   Haha yea I can’t figure out how that could possibly turn into money 
|   |   1 18.02.21 kagemaster  gnuq18e
|   |   |   Yesss, how???? 
|   |   |   1 18.02.21 Thypex  gnuu5xt
|   |   |   |   [видалено] 
|   |   |   |   1 18.02.21 None  gnvb85z
|   |   |   |   |   Damn, that's dope 
|   |   |   |   |   1 18.02.21 Thypex  gnvba11
I produce hip/hop beats and put them on websites like beatstars, fiverr, and pond5 and occasionally someone likes em enough to buy 
6 18.02.21 ichamp15  gnu1r4c
|   Cool!  Do you have a link to some of your work? 
|   1 18.02.21 Avocado_Aly  gnwnf44
|   |   Ill dm 
|   |   1 18.02.21 ichamp15  gnwnow3
Selling premium. It's not much now, but it has steadily grown. 
6 17.02.21 Jub-n-Jub  gnszyjs
|   Which stocks are your favorites? 
|   1 17.02.21 illupvoteforadollar  gntdh5d
|   |   MJ, PACB, SQ, IWM, PLTR, MSFT, PSTGSoon gonna break from PACB. Starting TAN and TER this week. Just started an experiment with TQQQ. I take half the profits from the premium and buy shares when it builds up enough. Selling premium has worked wonders leveling out my portfolio. I am dedicating about 10-15% of my portfolio to this. About another 5% to buying calls and puts. 1-3% on memes and the rest is to owning shares. 
|   |   4 17.02.21 Jub-n-Jub  gntmqh2
*onlyfans has entered the chat* 
7 17.02.21 whatitdobabeyyy  gnt9tn9
I agree 100%.I'm building out lead gen sites and ranking them so they can make me money while I sleep. Once they rank, I don't gotta fuss with them. I send the leads to local business owners every month and collect my money every month on autopilot. 
6 17.02.21 JzOzuna  gntgydp
|   Can you elaborate? How do these sites generate valuable leads if they aren't connected to a specific product or service? 
|   4 18.02.21 thehellcat  gntwngs
|   |   So the sites actually offer a certain service for example, pool cleaning. The site ranks, the leads go to a local business owner needing more leads and I collect my commission each month. I learned from Ippei Kanehara 
|   |   4 18.02.21 JzOzuna  gnw4sar
|   |   |   Can I DM you? I'm willing to pay for a consultation. 
|   |   |   3 21.02.21 joellecool  go7bwv7
|   |   |   |   Yea no problem, hit me up 
|   |   |   |   1 22.02.21 JzOzuna  gocdvg2
|   |   |   |   Yea np, hit me up 
|   |   |   |   1 22.02.21 JzOzuna  gocdx2c
|   |   |   How much are u making with these sites 
|   |   |   2 12.03.21 None  gqoiwa6
|   |   |   |   I've got 5 sites fully ranked, my goal is to have 10 more by the end of the year at the very least on page 1. I'm bringing it in a bit over $4K 
|   |   |   |   1 12.03.21 JzOzuna  gqp0p5n
|   |   |   |   |   Very awesome bro. How do the business owners know it was you who brought the sale? Promo offer mentioning your name? Like 5% off if u tell them I sent you. Or does it somehow show in the receipt? 
|   |   |   |   |   2 12.03.21 None  gqpa5t0
|   |   |   |   |   |   I use a call tracking software to forward the leads. When a business owner picks up the phone, the software tells them, "Call from..." Makes the process so much easier. I charge a monthly flat fee so, we don't need to worry about making sure I get paid for each job you know.That's what helps this be a passive income. 
|   |   |   |   |   |   1 12.03.21 JzOzuna  gqpayzy
Ask my boss 
6 17.02.21 Farge43  gntm0is
If you're in the US buy a house in an area where the locals are complaining about people coming from other states with their heathen money and sell a house for a profit you're comfortable with every two years. Keep doing that until you have enough money to buy a house outright. So you can have that huge extra chunk of money that would go to your mortage to invest, travel, or just play with while you're still young enough to enjoy life. It might take 10 to 15 years, and you'll still have to work, but it beats slogging away at your job that you're going to hate anyway to pay a mortgage off in 30 years in time to retire when you're much older and maybe don't have good enough health to enjoy your retirement anyway. You have a roof over head the bank can't take away. Plus you want to leave something for your kids or someone else when you go, you don't want to make your family pay for your funeral and settle your debts out of your estate. 
6 18.02.21 brickwall95  gnu97ee
8.6% APY on USD converted to USDC that just sits there. Can withdraw as often as needed. 
6 18.02.21 silversurfer08  gnut2t4
|   12% APY on USDT 
|   1 18.02.21 7ADARIII  gnvkwzh
|   |   Where? 👀 
|   |   2 18.02.21 silversurfer08  gnw9fu0
|   |   |   on blockchain 
|   |   |   1 18.02.21 7ADARIII  gnwar7o
|   |   |   |   how does this work? 
|   |   |   |   2 26.02.21 mangotease  gos6git
|   |   |   |   |   you get an annual interest on holding some of your crypto. the % varies from crypto to crypto and platform to platform. 
|   |   |   |   |   2 26.02.21 7ADARIII  goth05o
|   Where do you hold your USDC? 
|   1 03.03.21 poweredbyford87  gpkgtgy
|   |   Blockfi 
|   |   3 05.03.21 silversurfer08  gptwaso
|   |   |   Ah. Thank you good sir / madam 
|   |   |   2 06.03.21 poweredbyford87  gptzzbk
Mainly crypto. At worst, companies like NEXO are offering 10% APR on fiat currencies. At best, companies like YieldNodes have been providing me with \~10% a month. 
7 18.02.21 thisthomas  gnvefn7
|   But crypto is crazy at the moment, will your investments be affected if we hit a bear market? 
|   1 10.03.21 Doomsday40  gqf6eav
|   |   With companies like Nexo, I doubt it. With YieldNodes - potentially. Although the projects they’re working on have genuine usability outside of crypto markets. But it’s something to be mindful of. 
|   |   2 10.03.21 thisthomas  gqfby5q
Partnering with private lenders.  Fixed APR and the monthly income is nice.  I do literally nothing and the money comes in. 
5 17.02.21 JPDG  gnstdec
|   How did you get started? I’ve always been interested but haven’t found much aside from peer to peer lending 
|   3 17.02.21 _Qanukl3h3d_  gnsw1jl
|   How did you get started? I’ve always been interested but haven’t found much aside from peer to peer lending 
|   1 17.02.21 _Qanukl3h3d_  gnsw20z
|   P2P lending? Im curious 
|   1 17.02.21 Papa_Pazuzu  gnsw3fs
Local Lead Generation and holding BTC. 
5 17.02.21 Hatesville  gnsy9my
|   Could I PM you about Local Leads ? 
|   1 21.02.21 joellecool  go7bl5c
|   |   Shoot 
|   |   1 21.02.21 Hatesville  go7d9ei
|   |   |   for lead gen - do you mean advertising on fb/ig using the clients money to find them leads? 
|   |   |   1 26.02.21 mangotease  gos6doa
Markets are closed when I sleep so I don’t... better start staying up all night and sleep during the day 
4 17.02.21 CoffeeIsForEveryone  gnt3io6
I post stock pictures in the hive network, if you get curated than you make about 5-8€ in your sleep. I post blogs on publish0x that made me about 50cents in crypto each day, its not much but i just started out and I have a regular job .I can send you invites to both, in hive it actually helps registering over an invitation I can give you a kickstart buy upvoting your stuff 
5 18.02.21 Photo_film_  gntwiqu
Local Lead Generation. I build digital assets that bring in leads and partner with a local business owner to service them in return for a monthly fee - usually between $700-2500. It takes a bit of effort (and know-how) to pick the right combos and get the traffic flowing but once it's up and running, it's all passive from there (unless you count sending an invoice once a month).Admittedly, I have a few clients who I'll meet for coffee or spend time chatting with each month but that's because I genuinely enjoy hearing how they're doing.Really took off in the last 18 months and I've been able to generate a nice 5-figures a month and still adding more. I love being able to go on vacation or focus on other things and know the money will still be coming in. 
4 18.02.21 YelloRhinoDino  gnuiunc
|   I was once interesting in this but life got crazy and didn’t have the time, seeing your success. I might try and re-educate myself on this type of business. 
|   1 18.02.21 Boboded  gnurf8n
|   |   I know what you mean. That was me at first with lead gen but when I really decided to make it work, it took about 18 months of serious grind but it was so worth it. 
|   |   1 22.02.21 YelloRhinoDino  gob5z9v
|   Did you take a course or did you just learn by trial and error? 
|   1 21.02.21 None  go6fegr
|   Hello, I am super interested in this. Can I DM you? 
|   1 21.02.21 joellecool  go7cijt
|   Where did you learn to do this? 
|   0 18.02.21 terriblephotographs  gnvcm0a
|   |   I took a course by Ippei Kanehara after finding his blog.Learned everything I know from the dude and the others in the training group. Best education I could have asked for.If you want to learn about local lead gen, Google Ippei and check out the videos in the local lead gen - this is exactly the same stuff he taught me. 
|   |   1 22.02.21 YelloRhinoDino  gob5v89
I’m going to start selling options on stocks I own. I did some math and I could probably generate an extra $1k / month fairly low risk. 
3 18.02.21 Lifemacker  gnulcc8
|   Which stock you own? 
|   2 18.02.21 hitmastermoney  gnuoyya
E-commerce. 
5 18.02.21 vital-survivalist  gnuoc2d
|   Care to elaborate?! Like what platforms do you use? 
|   3 18.02.21 Candid-Anywhere is OP gnuq8hq
|   |   I use Shopify and occasionally ClickFunnels. My business is selling items online through the use of google and Facebook ads. 
|   |   2 18.02.21 vital-survivalist  gnusfod
|   |   |   Can I ask what type of product you sell? 
|   |   |   2 18.02.21 Candid-Anywhere is OP gnusioy
|   |   |   |   Sure my most successful store is based around unique lamps and LED products. 
|   |   |   |   5 18.02.21 vital-survivalist  gnusl25
|   |   |   |   |   Could i take a look, intrested on how you aproach this. 
|   |   |   |   |   2 18.02.21 Thypex  gnuuff2
|   |   |   |   |   |   I can definitely help out but won’t be mentioning my stores on Reddit. However I am planning on seeing interests and doing a webinar for how to do it all step by step. 
|   |   |   |   |   |   3 18.02.21 vital-survivalist  gnuwnej
|   |   |   |   |   |   |   Cool, you can dm me if you don't want to write it in the comments 
|   |   |   |   |   |   |   1 18.02.21 Thypex  gnuxb28
|   |   |   |   |   |   |   I'd be interested in that webinar! 
|   |   |   |   |   |   |   1 18.02.21 EndlessChaos_  gnw4dti
|   |   |   |   |   |   |   |   Thanks I’ll send you a link to sign up for when it goes live. 
|   |   |   |   |   |   |   |   1 18.02.21 vital-survivalist  gnweohj
|   |   |   |   |   |   |   |   |   Mildly interested too. I had a look at dropshipping, but couldn't figure out the expense ratio to break even. 
|   |   |   |   |   |   |   |   |   2 21.02.21 joellecool  go7bttg
|   |   |   |   |   |   |   |   |   |   You just need to figure out your cost per purchase and your roas 
|   |   |   |   |   |   |   |   |   |   1 02.03.21 vital-survivalist  gpgvmrw
|   |   |   |   |   Cool, thanks!! 
|   |   |   |   |   1 18.02.21 Candid-Anywhere is OP gnut48l
Crypto staking and yield farming.Making about 2k a month 
3 18.02.21 fxsnowy  gnw1tcd
|   Care to share more about it? I started with Nexo but have been looking at other options. At what starting amount are you seeing those returns? Thanks! 
|   1 11.03.21 tomsterpho  gqmqulc
Stonks 
2 17.02.21 Dick_8  gnsqqk2
By sleeping with other people 
2 17.02.21 Lvl1finalboss  gnt9ukg
I love working. 
2 17.02.21 None  gntfogj
He means investing. If you are not maxing out your 401k and/or Roth IRA contributions, that is where you should be starting. 
2 17.02.21 the_0rly_factor  gntfzya
I wonder if he actually said that and under what context. 
2 17.02.21 baummer  gntmfz4
Network / direct sales (once) for me - it's like 150€ a month right now plus my own consumer goods for free. I started at the end of last year. I know it is nothing too crazy, but I just sell / refer a product once and get my share month after month.My focus is more on the customer side and I only sell stuff that I genuinely believe in. My partner company even has a 30 day money back guarantee, even for used products, so I am cool with that. 
2 18.02.21 Cedrac  gntrzvq
Stocks..  book sales. Realestate appreciation growth and I have a women that cleans a daycare for me and it’s passive income 
2 18.02.21 ccashdan  gnujz1l
Stocks, real estate investments, bonds, money market accounts, savings accounts, CDs 
2 18.02.21 nearsingularity  gnv3uw2
By learning affiliate marketing, who wants to join me? Get in touch to find out more.. 
2 18.02.21 RiccardoJ17  gnvu677
|   [видалено] 
|   1 19.03.21 None  grgzr3h
I started selling designs on Redbubble and Teepublic.  Sometimes I wake up to find I’ve made a sale.  It’s super exciting, even when it’s just a sticker. 
2 18.02.21 crownnthistle  gnvy9dr
[видалено] 
2 18.02.21 None  gnw9s6m
|   I don’t understand this one. Can you clarify a bit more about what you do? 
|   2 18.02.21 vagabonn  gnwuidd
We just bought our first rental property this year, it’s appreciated about $30,000 in 8 months on top of the $400 we cash flow every month + mortgage pay down from the rent. 
2 11.03.21 IR1SHfighter  gqlkcw2
Trade for active income but have a system that allows entries to take about 1-3 days to exit from entry (somewhat passive).Acquire capital and buy index funds and rental properties. 
1 17.02.21 kingtechllc  gnsqwsc
Investing in Mutual funds. 
1 17.02.21 Fluffedbread  gntfll3
Started trading options and futures. Options trading has been great so far, weekly close to ATM calls, selling covered calls on stock I already own, might be getting into LEAPs and synthetic covered calls soon 
1 17.02.21 jerseyse410  gntov6v
between the wife and i, we have an ira (index funds and bonds), roth ira (mostly individual dividend stocks, some bonds) , 401k (some target date funds), a standard investment acct with mostly dividend stocks and somewhat steady growth funds, and another investment account with so-called volatile stocks to "gamble"/play around with. the "volatile" account I intend to just to give to my kid eventually in 10 years or so 
1 18.02.21 dogvenom  gntsm20
Landlord 
1 18.02.21 complexFLIPPER  gntwkxo
Remindme! 3 days 
1 18.02.21 cheesybread336  gnup29j
In my dreams. 
1 18.02.21 BernardoHuyser  gnv0q9p
Defi is the way ;) 
1 18.02.21 CrypticKache008  gnv65te
Remind me in 3 days 
1 18.02.21 staryny  gnv8ayz
I used to just host websites, and that’s pretty passive except for low support volume that I manage myself still... and now I sell websites, which I can then host if need be, and offer maintenance plans which I have fairly automated at this point, and I also sell plugin licenses, which has very low volume of support. Not 100% passive, but let’s just say I can have a lot of very slow days anytime I want. 
1 18.02.21 downtownrob  gnv8cj3
|   How do you find your clients? 
|   1 21.02.21 joellecool  go7c79e
|   |   I work with a lot of designers and copywriters, and they are constantly referring website design/dev clients, and from those I usually end up hosting quite a few, as well as maintenance. Plugins are found in the free repo, and have built-in dashboard upgrades to paid using Freemius.com. 
|   |   1 23.02.21 downtownrob  goft957
Remindme! 3 days 
1 18.02.21 staryny  gnv8d1c
[видалено] 
1 18.02.21 None  gnv9esh
|   What program? Is it free?? 
|   1 18.02.21 Candid-Anywhere is OP gnw2myz
|   |   Sounds too good to be true... might be wrong though 
|   |   1 18.02.21 Afonso0072001  gnw3yg8
|   |   |   Remindme! 2 days 
|   |   |   1 19.02.21 Random_dude_1980  go1vzhe
|   |   |   |   [видалено] 
|   |   |   |   1 23.02.21 None  gof948x
|   |   |   |   |   I set a reminder. It’s a Remindme bot 
|   |   |   |   |   1 23.02.21 Random_dude_1980  goftx0f
remindme! one week 
1 18.02.21 annieisawinchester  gnvbn7c
 Remindme! 2 days 
1 18.02.21 kosmoludek  gnvk4hf
Print on demand... I wake up most mornings having sold some of my photography on one of the platforms. It isn't quite enough yet, but it is growing. 
1 18.02.21 paulmp  gnvprbk
|   What platform do you use? 
|   1 18.02.21 4MelaZ  gnvulhq
|   |   Most of them, plus my own website that I've automated the ordering system in. 
|   |   2 19.02.21 paulmp  gnydba8
Passive income from dividends and DeFi. Currently making 6% passively from coinbase Algo token and about 7% on my dividend portfolio. Also I’m young so 10% of my portfolio is in hyper growth (yolo plays) that could make or break me while I also have a secondary account that is doing the same thing (turned 85-1.2k happy about that). Keep in mind, when I say yolo play I mean well calculated growth plays but are yolo because it could go up or down at the end of the day. 
1 18.02.21 randomsmiteplayer  gnw03fd
I have an app on Google play, Amazon and Apple,Started out 100usd a month 3.5 years ago. It's now making 1000usd a month give or take. Organic growth is amazing. I developed it and the wifey designed it. Family made passive income for life. 
1 19.02.21 shpatoza  go235ag
|   That’s awesome - congratulations! What is the app doing and how do you monetize it? Is it a paid app or are you offering pro/paid features? 
|   1 20.02.21 therealandinho  go2fz5w
|   |   It's a niche app for certain disability.It comes in a form of in app purchase for a lifetime usage or straight up paid.  No subscription as I feel it's not ok morally to charge monthly/annually for this type of app. I don't invest at all in ads or promotion. 
|   |   3 20.02.21 shpatoza  go3jgfz
facts 
1 20.02.21 Shermmmking  go2mlwz
I worked and invested into the markets 3 years ago, I make money in my sleep 
1 20.02.21 SpamSteal  go5ukdi
Well, tbh, warren byffet is still working his ass off so... find something you can do that doesnt make you want to blow your brains out. Man was meant to work. 
1 15.03.21 Sea-Veterinarian-333  gqznvl3
Currently dividends & music royalties (Global Rockstar) - looking to add more sources over time :-) 
1 18.04.21 mcpapaya  guzym32
-CryptoHopper bot trading through my Binance.US account(passively when I’m sleeping, always risks though and it’s a must that you have a strong interest in figuring it all out)-Lending my stock shares out from my Interactive Brokers account. Passive when short sellers borrow my shares and pay me and Interactive Brokers margin interest. Not reliable enough to predict as it is the market dynamics at work. Dividends from any stock holdings I have.-Holding crypto that throws off passive income by just owning it and it automatically gets reinvested or you can stake your crypto to earn interest too.-Credit cards that offer cash back rewards that exceed any annual fees they may or may not have(the government doesn’t pay me to use paper money and coins so then I don’t).-No real estate for me. I prefer highly liquid investments that I don’t have to get into debt to own. Although currently if you borrow $1 million+ from your margin brokerage account at Interactive Brokers they only charge 0.75% interest for the loan so there’s unlimited opportunities to arbitrage that rate to zero if you can find an investment that pays more interest than 0.75% interest but keeps your principal stable and liquid just in case the margin loan interest rate rises in the future. Margin interest is tax deductible too.-Having a spouse or partner that also has income helps you by lowering your daily, monthly, and annual expenses because they will be contributing to their fair share of all expenses as how a team should work. If there is no extra income from your spouse or partner then that just means that you will be financially responsible for everything. Can be a good thing or a bad thing as it depends on what other work your spouse or partner does in the day to day activities and operations around your place of residence that relieves you of those same responsibilities so you can focus on income generation. This generates income tax advantages if married obviously, saving on income tax expenses. 
1 09.07.21 Legitimate-Ad2825  h4jssrr
Minions. 
0 17.02.21 awardsurfer  gnsu9m3
Crypto and stonks! 
0 18.02.21 InsertCoin81  gnudcdu
A lot of what he says is bullshit.Some gold nuggets, but mostly exaggerated bullshit or things that only applied in the boomer economy of yesteryear.Even though I’m not much if a fan I’d still choose to take advice from Elon Musk over Buffett any day. 
-1 18.02.21 rwp80  gnu6mp8
|   I’d take advice from anyone who’s more successful than me. 
|   6 18.02.21 not-your-guru  gnvq4ak
|   |   Really, so you’d choose Buffett’s advice to go long on S&P500 instead of ratcheting healthy Crypto?Just because something made sense decades ago doesn’t mean it makes sense today.But hey, your choice, do what you like. 
|   |   0 19.02.21 rwp80  gnzeejb
|   |   |   I’d take his advice over some rando on Reddit. 
|   |   |   1 19.02.21 not-your-guru  gnzim6r
|   |   |   |   Haha what a dumb response. Okay, whatever floats your boat. 
|   |   |   |   0 19.02.21 rwp80  gnznp1z
|   |   |   |   |   Ignoring the advice of billionaires is pretty dumb too, but you do you :) 
|   |   |   |   |   1 19.02.21 not-your-guru  gnzo413
|   |   |   |   |   |   I cited Elon Musk as a better source of advice than Buffett. You clearly ignored that part of the comment. Read the comment, fool.Buffett net worth $85 billionMusk net worth $200 billionI prefer Musk’s more contemporary understanding of finance over Buffett any day. 
|   |   |   |   |   |   0 19.02.21 rwp80  go15j5z
|   |   |   |   |   |   |   If I were you, I’d worry more about running your business than being concerned with my opinions. Jim Rohn said that we are the average of the five people we spend time with.I’ve already given you more of my time than you deserve. Goodbye. ^(forever) 
|   |   |   |   |   |   |   2 19.02.21 not-your-guru  go16wok
|   |   |   |   |   |   |   |   Yes, please make it forever I'm tired of reading your nonsense at this point 
|   |   |   |   |   |   |   |   1 20.02.21 rwp80  go3olbf"""

point_character = """I have a few Instagram community pages that I schedule posts on. Not quite passive, but takes up 8-12 hours of solid work per week for around £13k a month. Super easy to do/start/grow. I started in January 2020 and stumbled on it by accident. I wake up to PayPal telling me I've been sent money everyday.. mostly because prime US time (my demographic) is when I sleep."""
string_list = string.split(point_character)[1]
print(string_list)