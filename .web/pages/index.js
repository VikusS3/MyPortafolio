
/** @jsxImportSource @emotion/react */import { Fragment } from "react"
import { Fragment_fd0e7cb8f9fb4669a6805377d925fba0 } from "/utils/stateful_components"
import { Box, HStack, Image as ChakraImage, Link, Spacer, Text, VStack } from "@chakra-ui/react"
import "focus-visible/dist/focus-visible"
import NextLink from "next/link"
import NextHead from "next/head"



export default function Component() {

  return (
    <Fragment>
  <Fragment_fd0e7cb8f9fb4669a6805377d925fba0/>
  <Box>
  <VStack sx={{"position": "sticky", "bg": "#132d46", "borderBottom": "0.25em solid #01c38e", "paddingX": "2em", "paddingY": "1em", "zIndex": 999, "top": 0, "width": "100%"}}>
  <HStack sx={{"width": "100%"}}>
  <ChakraImage alt={`Imagen con las letras VD`} src={`logo.png`} sx={{"width": "2em", "height": "2em"}}/>
  <Text>
  {`VikusDEV`}
</Text>
  <Spacer/>
  <Box sx={{"display": ["none", "block", "block", "block"]}}>
  <Link as={NextLink} className={`nes-icon linkedin is-medium`} href={`https://www.linkedin.com/in/felix-saul-orellana-contreras-971b042a6/`} isExternal={true}>
  {``}
</Link>
</Box>
  <Link as={NextLink} className={`nes-icon github is-medium`} href={`https://github.com/VikusS3`} isExternal={true}>
  {``}
</Link>
  <Link as={NextLink} className={`nes-icon gmail is-medium`} href={`felix21soc@gmail.com`} isExternal={true}>
  {``}
</Link>
</HStack>
</VStack>
</Box>
  <NextHead>
  <title>
  {`VikusDEV - Programador Full Stack`}
</title>
  <meta content={`VikusDEV es un programador freelance que se dedica al desarrollo web, diseño web, desarrollo de aplicaciones, desarrollo de software, desarrollo de apl`} name={`description`}/>
  <meta content={`favicon.ico`} property={`og:image`}/>
</NextHead>
</Fragment>
  )
}
